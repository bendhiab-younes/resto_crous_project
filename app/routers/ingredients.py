from typing import Annotated

from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.auth import exiger_connexion
from app.database import get_db
from app.models import Allergene, Ingredient
from app.templating import templates
from app.validation import lire_nombre

router = APIRouter(prefix="/ingredients", dependencies=[Depends(exiger_connexion)])

CHAMPS_NUMERIQUES = ("cout_par_kg", "calories", "proteines", "glucides", "lipides")
MESSAGE_NOM_PRIS = "Un ingrédient porte déjà ce nom."


# Tout est reçu en texte : une saisie invalide doit réafficher le formulaire, pas une erreur JSON.
class FormulaireIngredient(BaseModel):
    nom: str = ""
    cout_par_kg: str = ""
    calories: str = ""
    proteines: str = ""
    glucides: str = ""
    lipides: str = ""
    allergenes: list[str] = []


def tous_les_allergenes(db: Session) -> list[Allergene]:
    return list(db.scalars(select(Allergene).order_by(Allergene.nom)))


def saisie_depuis(ingredient: Ingredient | None) -> dict:
    if ingredient is None:
        return FormulaireIngredient().model_dump()
    return {
        "nom": ingredient.nom,
        **{champ: str(getattr(ingredient, champ)) for champ in CHAMPS_NUMERIQUES},
        "allergenes": [str(allergene.id) for allergene in ingredient.allergenes],
    }


def afficher_formulaire(
    request: Request,
    db: Session,
    ingredient: Ingredient | None,
    saisie: dict,
    erreurs: dict[str, str] | None = None,
) -> HTMLResponse:
    return templates.TemplateResponse(
        request,
        "ingredients/formulaire.html",
        {
            "ingredient": ingredient,
            "allergenes": tous_les_allergenes(db),
            "saisie": saisie,
            "erreurs": erreurs or {},
        },
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT if erreurs else status.HTTP_200_OK,
    )


def afficher_liste(
    request: Request, db: Session, erreur: str | None = None, status_code: int = status.HTTP_200_OK
) -> HTMLResponse:
    ingredients = db.scalars(select(Ingredient).order_by(Ingredient.nom)).all()
    return templates.TemplateResponse(
        request,
        "ingredients/liste.html",
        {"ingredients": ingredients, "erreur": erreur},
        status_code=status_code,
    )


def ingredient_ou_404(db: Session, ingredient_id: int) -> Ingredient:
    ingredient = db.get(Ingredient, ingredient_id)
    if ingredient is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return ingredient


def valider(
    db: Session, formulaire: FormulaireIngredient, ingredient: Ingredient | None
) -> tuple[dict, dict[str, str]]:
    erreurs: dict[str, str] = {}
    nom = formulaire.nom.strip()
    if not nom:
        erreurs["nom"] = "Le nom est obligatoire."
    else:
        meme_nom = db.scalar(select(Ingredient).where(func.lower(Ingredient.nom) == nom.lower()))
        if meme_nom is not None and meme_nom is not ingredient:
            erreurs["nom"] = MESSAGE_NOM_PRIS

    valeurs: dict = {"nom": nom}
    for champ in CHAMPS_NUMERIQUES:
        nombre = lire_nombre(getattr(formulaire, champ))
        if nombre is None:
            erreurs[champ] = "Saisir un nombre."
        elif nombre < 0:
            erreurs[champ] = (
                "Le coût ne peut pas être négatif."
                if champ == "cout_par_kg"
                else "La valeur ne peut pas être négative."
            )
        valeurs[champ] = nombre

    allergenes = {str(allergene.id): allergene for allergene in tous_les_allergenes(db)}
    if any(identifiant not in allergenes for identifiant in formulaire.allergenes):
        erreurs["allergenes"] = "Allergène inconnu."
    else:
        valeurs["allergenes"] = [allergenes[identifiant] for identifiant in formulaire.allergenes]

    return valeurs, erreurs


def enregistrer(
    request: Request, db: Session, formulaire: FormulaireIngredient, ingredient: Ingredient | None
) -> HTMLResponse | RedirectResponse:
    valeurs, erreurs = valider(db, formulaire, ingredient)
    if not erreurs:
        cible = ingredient or Ingredient()
        for champ, valeur in valeurs.items():
            setattr(cible, champ, valeur)
        db.add(cible)
        try:
            db.commit()
        except IntegrityError:
            db.rollback()
            erreurs["nom"] = MESSAGE_NOM_PRIS
    if erreurs:
        return afficher_formulaire(request, db, ingredient, formulaire.model_dump(), erreurs)
    return RedirectResponse("/ingredients", status_code=status.HTTP_303_SEE_OTHER)


@router.get("", response_class=HTMLResponse)
def liste(request: Request, db: Session = Depends(get_db)):
    return afficher_liste(request, db)


@router.get("/nouveau", response_class=HTMLResponse)
def nouveau(request: Request, db: Session = Depends(get_db)):
    return afficher_formulaire(request, db, None, saisie_depuis(None))


@router.post("", response_class=HTMLResponse)
def creer(
    request: Request,
    formulaire: Annotated[FormulaireIngredient, Form()],
    db: Session = Depends(get_db),
):
    return enregistrer(request, db, formulaire, None)


@router.get("/{ingredient_id}", response_class=HTMLResponse)
def detail(request: Request, ingredient_id: int, db: Session = Depends(get_db)):
    ingredient = ingredient_ou_404(db, ingredient_id)
    return afficher_formulaire(request, db, ingredient, saisie_depuis(ingredient))


@router.post("/{ingredient_id}", response_class=HTMLResponse)
def modifier(
    request: Request,
    ingredient_id: int,
    formulaire: Annotated[FormulaireIngredient, Form()],
    db: Session = Depends(get_db),
):
    return enregistrer(request, db, formulaire, ingredient_ou_404(db, ingredient_id))


@router.post("/{ingredient_id}/supprimer", response_class=HTMLResponse)
def supprimer(request: Request, ingredient_id: int, db: Session = Depends(get_db)):
    db.delete(ingredient_ou_404(db, ingredient_id))
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        return afficher_liste(
            request,
            db,
            erreur="Cet ingrédient est utilisé dans une recette : suppression impossible.",
            status_code=status.HTTP_409_CONFLICT,
        )
    return RedirectResponse("/ingredients", status_code=status.HTTP_303_SEE_OTHER)
