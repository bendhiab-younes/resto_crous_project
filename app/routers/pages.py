from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import get_db
from app.templating import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def accueil(request: Request):
    return templates.TemplateResponse(request, "accueil.html")


@router.get("/sante")
def sante(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"statut": "ok"}
