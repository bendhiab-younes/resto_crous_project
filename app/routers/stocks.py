from typing import Annotated

from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.auth import exiger_role
from app.database import get_db
from app.models import Ingredient, Role, Stock
from app.templating import templates
from app.validation import lire_nombre

router = APIRouter(prefix="/stocks", dependencies=[Depends(exiger_role(Role.INTENDANT))])


class FormulaireStock(BaseModel):
    quantite_disponible: str = ""
    seuil_alerte: str = ""


def ingredient_ou_404(db: Session, ingredient_id: int) -> Ingredient:
    ingredient = db.get(Ingredient, ingredient_id)
    if ingredient is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return ingredient


def afficher_formulaire(
    request: Request,
    ingredient: Ingredient,
    saisie: dict[str, str],
    erreurs: dict[str, str] | None = None,
) -> HTMLResponse:
    return templates.TemplateResponse(
        request,
        "stocks/formulaire.html",
        {
            "ingredient": ingredient,
            "saisie": saisie,
            "erreurs": erreurs or {},
        },
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT if erreurs else status.HTTP_200_OK,
    )


def saisie_depuis(stock: Stock | None) -> dict[str, str]:
    if stock is None:
        return FormulaireStock().model_dump()
    return {
        "quantite_disponible": str(stock.quantite_disponible),
        "seuil_alerte": str(stock.seuil_alerte),
    }


def valider(formulaire: FormulaireStock) -> tuple[dict[str, float], dict[str, str]]:
    erreurs: dict[str, str] = {}
    valeurs: dict[str, float] = {}
    for champ in ("quantite_disponible", "seuil_alerte"):
        nombre = lire_nombre(getattr(formulaire, champ))
        if nombre is None:
            erreurs[champ] = "Saisir un nombre."
        elif nombre < 0:
            erreurs[champ] = "La valeur ne peut pas être négative."
        else:
            valeurs[champ] = nombre
    return valeurs, erreurs


@router.get("", response_class=HTMLResponse)
def liste(request: Request, db: Session = Depends(get_db)):
    ingredients = db.scalars(select(Ingredient).order_by(Ingredient.nom)).all()
    stocks = {
        stock.ingredient_id: stock
        for stock in db.scalars(select(Stock))
    }
    lignes = [{"ingredient": ingredient, "stock": stocks.get(ingredient.id)} for ingredient in ingredients]
    return templates.TemplateResponse(request, "stocks/liste.html", {"lignes": lignes})


@router.get("/{ingredient_id}", response_class=HTMLResponse)
def detail(request: Request, ingredient_id: int, db: Session = Depends(get_db)):
    ingredient = ingredient_ou_404(db, ingredient_id)
    stock = db.scalar(select(Stock).where(Stock.ingredient_id == ingredient_id))
    return afficher_formulaire(request, ingredient, saisie_depuis(stock))


@router.post("/{ingredient_id}", response_class=HTMLResponse)
def modifier(
    request: Request,
    ingredient_id: int,
    formulaire: Annotated[FormulaireStock, Form()],
    db: Session = Depends(get_db),
):
    ingredient = ingredient_ou_404(db, ingredient_id)
    valeurs, erreurs = valider(formulaire)
    if erreurs:
        return afficher_formulaire(request, ingredient, formulaire.model_dump(), erreurs)

    stock = db.scalar(select(Stock).where(Stock.ingredient_id == ingredient_id))
    if stock is None:
        stock = Stock(ingredient=ingredient)
    for champ, valeur in valeurs.items():
        setattr(stock, champ, valeur)
    db.add(stock)
    db.commit()
    return RedirectResponse("/stocks", status_code=status.HTTP_303_SEE_OTHER)
