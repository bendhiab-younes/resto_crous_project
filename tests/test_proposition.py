import pytest

from app.models import Ingredient, LigneRecette, Recette, Role, StatutRecette, TypePlat


@pytest.fixture
def recette(db, utilisateur):
    ingredient = Ingredient(
        nom="Farine", cout_par_kg=1, calories=100, proteines=1, glucides=1, lipides=1
    )
    plat = Recette(
        titre="Crêpes",
        type=TypePlat.VEGETARIEN,
        vegetarien=True,
        procedure="Mélanger.",
        auteur=utilisateur,
        lignes=[LigneRecette(ingredient=ingredient, quantite=250)],
    )
    db.add(plat)
    db.commit()
    return plat


def proposer(client, recette):
    return client.post(f"/recettes/{recette.id}/proposer", follow_redirects=False)


def test_TC_S06_01_proposer_une_recette_en_brouillon(client_connecte, db, recette):
    reponse = proposer(client_connecte, recette)

    assert reponse.status_code == 303
    assert reponse.headers["location"] == f"/recettes/{recette.id}/fiche"
    db.refresh(recette)
    assert recette.statut is StatutRecette.A_VALIDER


@pytest.mark.parametrize(
    "statut", [StatutRecette.A_VALIDER, StatutRecette.VALIDEE, StatutRecette.REFUSEE]
)
def test_TC_S06_02_seul_un_brouillon_peut_etre_propose(client_connecte, db, recette, statut):
    recette.statut = statut
    db.commit()

    reponse = proposer(client_connecte, recette)

    assert reponse.status_code == 409
    assert "Seule une recette en brouillon peut être proposée." in reponse.text
    db.refresh(recette)
    assert recette.statut is statut


def test_TC_S06_03_proposition_refusee_a_un_autre_role(client_avec_role, db, recette):
    reponse = proposer(client_avec_role(Role.INTENDANT), recette)

    assert reponse.status_code == 403
    assert "text/html" in reponse.headers["content-type"]
    assert "Accès refusé" in reponse.text
    db.refresh(recette)
    assert recette.statut is StatutRecette.BROUILLON


def test_TC_S06_04_proposition_sans_session(client, db, recette):
    reponse = proposer(client, recette)

    assert reponse.status_code == 303
    assert reponse.headers["location"] == "/connexion"
    db.refresh(recette)
    assert recette.statut is StatutRecette.BROUILLON


def test_TC_S06_05_recette_inexistante_404(client_connecte):
    assert client_connecte.post("/recettes/999/proposer").status_code == 404


def fiche(client, recette):
    return client.get(f"/recettes/{recette.id}/fiche").text


def test_TC_S06_06_bouton_visible_pour_le_chef_sur_un_brouillon(client_connecte, recette):
    assert f"/recettes/{recette.id}/proposer" in fiche(client_connecte, recette)


def test_TC_S06_07_bouton_masque_une_fois_proposee(client_connecte, db, recette):
    recette.statut = StatutRecette.A_VALIDER
    db.commit()

    assert f"/recettes/{recette.id}/proposer" not in fiche(client_connecte, recette)


def test_TC_S06_08_bouton_masque_pour_un_autre_role(client_avec_role, recette):
    assert f"/recettes/{recette.id}/proposer" not in fiche(
        client_avec_role(Role.INTENDANT), recette
    )


def test_TC_S06_09_statut_affiche_sur_la_fiche(client_connecte, db, recette):
    recette.statut = StatutRecette.A_VALIDER
    db.commit()

    assert "À valider" in fiche(client_connecte, recette)
