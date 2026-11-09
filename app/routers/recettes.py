from itertools import zip_longest
from typing import Annotated

from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.auth import exiger_connexion, exiger_role
from app.calculs import allergenes_recette, cout_recette, nutrition_pour_100g
from app.database import get_db
from app.models import (
    Ingredient,
    LigneRecette,
    Recette,
    Role,
    StatutRecette,
    TypePlat,
    Utilisateur,
)
from app.templating import templates
from app.validation import lire_nombre

router = APIRouter(prefix="/recettes", dependencies=[Depends(exiger_connexion)])

MESSAGE_QUANTITE = "La quantité doit être un nombre positif, en grammes."


class FormulaireRecette(BaseModel):
    titre: str = ""
    type: str = ""
    vegetarien: str = ""
    procedure: str = ""
    ingredient_id: list[str] = []
    quantite: list[str] = []


def saisie_depuis_formulaire(formulaire: FormulaireRecette) -> dict:
    return {
        "titre": formulaire.titre,
        "type": formulaire.type,
        "vegetarien": bool(formulaire.vegetarien),
        "procedure": formulaire.procedure,
        "lignes": [
            {"ingredient_id": ingredient_id, "quantite": quantite}
            for ingredient_id, quantite in lignes_saisies(formulaire)
        ],
    }


def saisie_depuis(recette: Recette | None) -> dict:
    if recette is None:
        return saisie_depuis_formulaire(FormulaireRecette())
    return {
        "titre": recette.titre,
        "type": recette.type.value,
        "vegetarien": recette.vegetarien,
        "procedure": recette.procedure,
        "lignes": [
            {"ingredient_id": str(ligne.ingredient_id), "quantite": str(ligne.quantite)}
            for ligne in recette.lignes
        ],
    }


def lignes_saisies(formulaire: FormulaireRecette) -> list[tuple[str, str]]:
    """Les paires (ingrédient, quantité), sans les lignes laissées vides dans le formulaire."""
    paires = zip_longest(formulaire.ingredient_id, formulaire.quantite, fillvalue="")
    return [(i.strip(), q.strip()) for i, q in paires if i.strip() or q.strip()]


def afficher_formulaire(
    request: Request,
    db: Session,
    recette: Recette | None,
    saisie: dict,
    erreurs: dict[str, str] | None = None,
) -> HTMLResponse:
    return templates.TemplateResponse(
        request,
        "recettes/formulaire.html",
        {
            "recette": recette,
            "ingredients": db.scalars(select(Ingredient).order_by(Ingredient.nom)).all(),
            "types": [type_plat.value for type_plat in TypePlat],
            "saisie": saisie,
            "erreurs": erreurs or {},
        },
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT if erreurs else status.HTTP_200_OK,
    )


def recette_ou_404(db: Session, recette_id: int) -> Recette:
    recette = db.get(Recette, recette_id)
    if recette is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return recette


def afficher_fiche(
    request: Request,
    recette: Recette,
    erreur: str | None = None,
    status_code: int = status.HTTP_200_OK,
) -> HTMLResponse:
    return templates.TemplateResponse(
        request,
        "recettes/fiche.html",
        {
            "recette": recette,
            "cout": cout_recette(recette.lignes),
            "nutrition": nutrition_pour_100g(recette.lignes),
            "allergenes": allergenes_recette(recette.lignes),
            "erreur": erreur,
        },
        status_code=status_code,
    )


def valider_lignes(
    db: Session, formulaire: FormulaireRecette
) -> tuple[list[LigneRecette], str | None]:
    saisies = lignes_saisies(formulaire)
    if not saisies:
        return [], "Ajouter au moins un ingrédient."

    ingredients = {str(ingredient.id): ingredient for ingredient in db.scalars(select(Ingredient))}
    lignes = []
    for ingredient_id, quantite_saisie in saisies:
        if ingredient_id not in ingredients:
            return [], "Ingrédient inconnu."
        quantite = lire_nombre(quantite_saisie)
        if quantite is None or quantite <= 0:
            return [], MESSAGE_QUANTITE
        lignes.append(LigneRecette(ingredient=ingredients[ingredient_id], quantite=quantite))
    return lignes, None


def valider(
    db: Session, formulaire: FormulaireRecette
) -> tuple[dict, list[LigneRecette], dict[str, str]]:
    erreurs: dict[str, str] = {}
    titre = formulaire.titre.strip()
    if not titre:
        erreurs["titre"] = "Le titre est obligatoire."
    procedure = formulaire.procedure.strip()
    if not procedure:
        erreurs["procedure"] = "La procédure est obligatoire."
    if formulaire.type not in TypePlat.__members__:
        erreurs["type"] = "Type de plat inconnu."

    lignes, erreur_lignes = valider_lignes(db, formulaire)
    if erreur_lignes:
        erreurs["lignes"] = erreur_lignes

    valeurs = {
        "titre": titre,
        "type": formulaire.type,
        "vegetarien": bool(formulaire.vegetarien),
        "procedure": procedure,
    }
    return valeurs, lignes, erreurs


def enregistrer(
    request: Request,
    db: Session,
    formulaire: FormulaireRecette,
    recette: Recette | None,
    auteur: Utilisateur,
) -> HTMLResponse | RedirectResponse:
    valeurs, lignes, erreurs = valider(db, formulaire)
    if erreurs:
        saisie = saisie_depuis_formulaire(formulaire)
        return afficher_formulaire(request, db, recette, saisie, erreurs)

    cible = recette or Recette(auteur=auteur)
    for champ, valeur in valeurs.items():
        setattr(cible, champ, valeur)
    cible.lignes = lignes
    db.add(cible)
    db.commit()
    return RedirectResponse("/recettes", status_code=status.HTTP_303_SEE_OTHER)


@router.get("", response_class=HTMLResponse)
def liste(request: Request, db: Session = Depends(get_db)):
    recettes = db.scalars(select(Recette).order_by(Recette.titre)).all()
    return templates.TemplateResponse(request, "recettes/liste.html", {"recettes": recettes})


@router.get("/nouveau", response_class=HTMLResponse)
def nouveau(request: Request, db: Session = Depends(get_db)):
    return afficher_formulaire(request, db, None, saisie_depuis(None))


@router.post("", response_class=HTMLResponse)
def creer(
    request: Request,
    formulaire: Annotated[FormulaireRecette, Form()],
    db: Session = Depends(get_db),
    auteur: Utilisateur = Depends(exiger_connexion),
):
    return enregistrer(request, db, formulaire, None, auteur)


@router.get("/{recette_id}/fiche", response_class=HTMLResponse)
def fiche(request: Request, recette_id: int, db: Session = Depends(get_db)):
    return afficher_fiche(request, recette_ou_404(db, recette_id))


@router.post(
    "/{recette_id}/proposer",
    response_class=HTMLResponse,
    dependencies=[Depends(exiger_role(Role.CHEF))],
)
def proposer(request: Request, recette_id: int, db: Session = Depends(get_db)):
    recette = recette_ou_404(db, recette_id)
    if recette.statut is not StatutRecette.BROUILLON:
        return afficher_fiche(
            request,
            recette,
            erreur="Seule une recette en brouillon peut être proposée.",
            status_code=status.HTTP_409_CONFLICT,
        )
    recette.statut = StatutRecette.A_VALIDER
    db.commit()
    return RedirectResponse(f"/recettes/{recette.id}/fiche", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/{recette_id}", response_class=HTMLResponse)
def detail(request: Request, recette_id: int, db: Session = Depends(get_db)):
    recette = recette_ou_404(db, recette_id)
    return afficher_formulaire(request, db, recette, saisie_depuis(recette))


@router.post("/{recette_id}", response_class=HTMLResponse)
def modifier(
    request: Request,
    recette_id: int,
    formulaire: Annotated[FormulaireRecette, Form()],
    db: Session = Depends(get_db),
    auteur: Utilisateur = Depends(exiger_connexion),
):
    return enregistrer(request, db, formulaire, recette_ou_404(db, recette_id), auteur)


@router.post("/{recette_id}/supprimer")
def supprimer(recette_id: int, db: Session = Depends(get_db)):
    db.delete(recette_ou_404(db, recette_id))
    db.commit()
    return RedirectResponse("/recettes", status_code=status.HTTP_303_SEE_OTHER)
