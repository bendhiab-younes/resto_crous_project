import pytest

from app.models import Ingredient, LigneRecette, Recette, StatutRecette, TypePlat


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
        statut=StatutRecette.VALIDEE,
        auteur=utilisateur,
        lignes=[LigneRecette(ingredient=ingredient, quantite=250)],
    )
    db.add(plat)
    db.commit()
    return plat


def telecharger(client, recette):
    return client.get(f"/recettes/{recette.id}/pdf", follow_redirects=False)


def test_TC_S17_03_telechargement_d_une_recette_validee(client_connecte, recette):
    reponse = telecharger(client_connecte, recette)

    assert reponse.status_code == 200
    assert reponse.headers["content-type"] == "application/pdf"
    assert f'recette-{recette.id}.pdf' in reponse.headers["content-disposition"]
    assert reponse.content.startswith(b"%PDF")


@pytest.mark.parametrize(
    "statut", [StatutRecette.BROUILLON, StatutRecette.A_VALIDER, StatutRecette.REFUSEE]
)
def test_TC_S17_04_seule_une_recette_validee_est_imprimable(client_connecte, db, recette, statut):
    recette.statut = statut
    db.commit()

    reponse = telecharger(client_connecte, recette)

    assert reponse.status_code == 409
    assert "Seule une recette validée peut être imprimée." in reponse.text


def test_TC_S17_05_recette_inexistante_404(client_connecte):
    assert client_connecte.get("/recettes/999/pdf").status_code == 404


def test_TC_S17_06_telechargement_sans_session(client, recette):
    assert telecharger(client, recette).status_code == 303


def test_TC_S17_07_lien_visible_sur_une_recette_validee(client_connecte, recette):
    assert f"/recettes/{recette.id}/pdf" in client_connecte.get(f"/recettes/{recette.id}/fiche").text


def test_TC_S17_08_lien_masque_sur_un_brouillon(client_connecte, db, recette):
    recette.statut = StatutRecette.BROUILLON
    db.commit()

    assert f"/recettes/{recette.id}/pdf" not in client_connecte.get(
        f"/recettes/{recette.id}/fiche"
    ).text
