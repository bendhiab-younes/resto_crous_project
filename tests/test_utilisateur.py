import pytest
from sqlalchemy.exc import IntegrityError

from app.models import Role, Utilisateur


def creer_utilisateur(db, identifiant="chef", mot_de_passe="secret"):
    utilisateur = Utilisateur(identifiant=identifiant, role=Role.CHEF)
    utilisateur.definir_mot_de_passe(mot_de_passe)
    db.add(utilisateur)
    db.commit()
    return utilisateur


def test_TC_S01_01_mot_de_passe_stocke_hache(db):
    utilisateur = creer_utilisateur(db, mot_de_passe="secret")

    assert "secret" not in utilisateur.mot_de_passe_hache


def test_TC_S01_02_verification_du_mot_de_passe(db):
    utilisateur = creer_utilisateur(db, mot_de_passe="secret")

    assert utilisateur.verifier_mot_de_passe("secret")
    assert not utilisateur.verifier_mot_de_passe("autre")


def test_TC_S01_03_deux_hachages_du_meme_mot_de_passe_different(db):
    premier = creer_utilisateur(db, identifiant="a", mot_de_passe="secret")
    second = creer_utilisateur(db, identifiant="b", mot_de_passe="secret")

    assert premier.mot_de_passe_hache != second.mot_de_passe_hache


def test_TC_S01_04_identifiant_unique(db):
    creer_utilisateur(db, identifiant="chef")

    with pytest.raises(IntegrityError):
        creer_utilisateur(db, identifiant="chef")
