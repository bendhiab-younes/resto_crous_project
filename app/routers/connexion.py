import secrets

from fastapi import APIRouter, Depends, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.auth import COOKIE_SESSION
from app.database import get_db
from app.models import SessionUtilisateur, Utilisateur
from app.securite import hacher_mot_de_passe, verifier_mot_de_passe
from app.templating import templates

router = APIRouter()

MESSAGE_ECHEC = "Identifiant ou mot de passe incorrect."
# Vérifié quand le compte n'existe pas, pour que la durée de réponse ne le révèle pas.
HACHE_LEURRE = hacher_mot_de_passe(secrets.token_urlsafe())


def identifiants_valides(utilisateur: Utilisateur | None, mot_de_passe: str) -> bool:
    if utilisateur is None:
        verifier_mot_de_passe(mot_de_passe, HACHE_LEURRE)
        return False
    return utilisateur.verifier_mot_de_passe(mot_de_passe)


@router.get("/connexion", response_class=HTMLResponse)
def page_connexion(request: Request):
    return templates.TemplateResponse(request, "connexion.html", {"erreur": None})


@router.post("/connexion", response_class=HTMLResponse)
def connexion(
    request: Request,
    identifiant: str = Form(""),
    mot_de_passe: str = Form(""),
    db: Session = Depends(get_db),
):
    utilisateur = db.scalar(select(Utilisateur).where(Utilisateur.identifiant == identifiant))
    if not identifiants_valides(utilisateur, mot_de_passe):
        return templates.TemplateResponse(
            request,
            "connexion.html",
            {"erreur": MESSAGE_ECHEC},
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    jeton = secrets.token_urlsafe(32)
    db.add(SessionUtilisateur(jeton=jeton, utilisateur_id=utilisateur.id))
    db.commit()
    reponse = RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)
    reponse.set_cookie(COOKIE_SESSION, jeton, httponly=True, samesite="lax")
    return reponse


@router.post("/deconnexion")
def deconnexion(request: Request, db: Session = Depends(get_db)):
    jeton = request.cookies.get(COOKIE_SESSION)
    session = db.get(SessionUtilisateur, jeton) if jeton else None
    if session is not None:
        db.delete(session)
        db.commit()
    reponse = RedirectResponse("/connexion", status_code=status.HTTP_303_SEE_OTHER)
    reponse.delete_cookie(COOKIE_SESSION)
    return reponse
