from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.auth import exiger_role
from app.calculs import (
    allergenes_recette,
    cout_recette,
    ingredients_manquants,
    nutrition_pour_100g,
)
from app.database import get_db
from app.models import Recette, Role, StatutRecette, Stock
from app.templating import templates

router = APIRouter(prefix="/validations", dependencies=[Depends(exiger_role(Role.INTENDANT))])


def recette_a_valider_ou_404(db: Session, recette_id: int) -> Recette:
    recette = db.get(Recette, recette_id)
    if recette is None or recette.statut is not StatutRecette.A_VALIDER:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return recette


def manquants(db: Session, recette: Recette) -> list[str]:
    stocks = {stock.ingredient_id: stock.quantite_disponible for stock in db.scalars(select(Stock))}
    return ingredients_manquants(recette.lignes, stocks)


def afficher_detail(
    request: Request,
    db: Session,
    recette: Recette,
    motif: str = "",
    erreurs: dict[str, str] | None = None,
    status_code: int = status.HTTP_200_OK,
) -> HTMLResponse:
    return templates.TemplateResponse(
        request,
        "validations/detail.html",
        {
            "recette": recette,
            "cout": cout_recette(recette.lignes),
            "nutrition": nutrition_pour_100g(recette.lignes),
            "allergenes": allergenes_recette(recette.lignes),
            "manquants": manquants(db, recette),
            "saisie": {"motif": motif},
            "erreurs": erreurs or {},
        },
        status_code=status_code,
    )


@router.get("", response_class=HTMLResponse)
def liste(request: Request, db: Session = Depends(get_db)):
    recettes = db.scalars(
        select(Recette).where(Recette.statut == StatutRecette.A_VALIDER).order_by(Recette.titre)
    ).all()
    return templates.TemplateResponse(request, "validations/liste.html", {"recettes": recettes})


@router.get("/{recette_id}", response_class=HTMLResponse)
def detail(request: Request, recette_id: int, db: Session = Depends(get_db)):
    return afficher_detail(request, db, recette_a_valider_ou_404(db, recette_id))


@router.post("/{recette_id}/valider", response_class=HTMLResponse)
def valider(request: Request, recette_id: int, db: Session = Depends(get_db)):
    recette = recette_a_valider_ou_404(db, recette_id)
    if manquants(db, recette):
        return afficher_detail(
            request,
            db,
            recette,
            erreurs={"validation": "Stock insuffisant : la recette ne peut pas être validée."},
            status_code=status.HTTP_409_CONFLICT,
        )
    recette.statut = StatutRecette.VALIDEE
    db.commit()
    return RedirectResponse("/validations", status_code=status.HTTP_303_SEE_OTHER)


@router.post("/{recette_id}/refuser", response_class=HTMLResponse)
def refuser(
    request: Request, recette_id: int, motif: str = Form(""), db: Session = Depends(get_db)
):
    recette = recette_a_valider_ou_404(db, recette_id)
    motif_nettoye = motif.strip()
    if not motif_nettoye:
        return afficher_detail(
            request,
            db,
            recette,
            erreurs={"motif": "Le motif est obligatoire."},
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        )
    recette.statut = StatutRecette.REFUSEE
    recette.motif_refus = motif_nettoye
    db.commit()
    return RedirectResponse("/validations", status_code=status.HTTP_303_SEE_OTHER)
