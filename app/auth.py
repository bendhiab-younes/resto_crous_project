from fastapi import Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import SessionUtilisateur, Utilisateur

COOKIE_SESSION = "session"


def utilisateur_connecte(request: Request, db: Session = Depends(get_db)) -> Utilisateur | None:
    jeton = request.cookies.get(COOKIE_SESSION)
    session = db.get(SessionUtilisateur, jeton) if jeton else None
    utilisateur = session.utilisateur if session else None
    # Lu par base.html pour afficher la navigation.
    request.state.utilisateur = utilisateur
    return utilisateur


def exiger_connexion(utilisateur: Utilisateur | None = Depends(utilisateur_connecte)) -> Utilisateur:
    if utilisateur is None:
        raise HTTPException(status.HTTP_303_SEE_OTHER, headers={"Location": "/connexion"})
    return utilisateur
