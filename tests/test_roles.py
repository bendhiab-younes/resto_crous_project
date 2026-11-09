import pytest
from fastapi import HTTPException

from app.auth import exiger_role
from app.changer_role import changer_role
from app.models import Role, Utilisateur


def test_TC_S05_01_role_autorise():
    compte = Utilisateur(identifiant="a", role=Role.INTENDANT)

    assert exiger_role(Role.INTENDANT)(compte) is compte


def test_TC_S05_02_plusieurs_roles_autorises():
    compte = Utilisateur(identifiant="a", role=Role.CHEF)

    assert exiger_role(Role.INTENDANT, Role.CHEF)(compte) is compte


def test_TC_S05_03_role_refuse():
    compte = Utilisateur(identifiant="a", role=Role.CHEF)

    with pytest.raises(HTTPException) as erreur:
        exiger_role(Role.INTENDANT)(compte)

    assert erreur.value.status_code == 403


def test_TC_S05_04_changer_le_role_d_un_compte(db, utilisateur):
    changer_role(db, "chef", Role.INTENDANT)

    db.refresh(utilisateur)
    assert utilisateur.role is Role.INTENDANT


def test_TC_S05_05_changer_le_role_d_un_compte_inconnu(db, utilisateur):
    with pytest.raises(ValueError):
        changer_role(db, "inconnu", Role.INTENDANT)

    db.refresh(utilisateur)
    assert utilisateur.role is Role.CHEF


@pytest.mark.parametrize("role", [Role.CHEF, Role.INTENDANT, Role.GESTION_CENTRALE])
def test_TC_S05_08_chaque_role_peut_etre_attribue(db, utilisateur, role):
    changer_role(db, "chef", role)

    db.refresh(utilisateur)
    assert utilisateur.role is role
