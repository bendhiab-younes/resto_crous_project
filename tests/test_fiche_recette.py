import pytest

from app.models import Allergene, Ingredient, LigneRecette, Recette, TypePlat


def ajouter_ingredient(db, nom, cout, nutrition, allergenes=()):
    calories, proteines, glucides, lipides = nutrition
    ingredient = Ingredient(
        nom=nom,
        cout_par_kg=cout,
        calories=calories,
        proteines=proteines,
        glucides=glucides,
        lipides=lipides,
        allergenes=[Allergene(nom=allergene) for allergene in allergenes],
    )
    db.add(ingredient)
    db.commit()
    return ingredient


@pytest.fixture
def recette(db, utilisateur):
    # Attendu, calculé à la main sur 500 g : coût 200/1000 × 2 + 300/1000 × 1 = 0,70 ;
    # calories (200 × 300 + 300 × 50) / 500 = 150 ; protéines (200 × 10 + 300 × 5) / 500 = 7 ;
    # glucides (200 × 70 + 300 × 5) / 500 = 31 ; lipides (200 × 1 + 300 × 2,5) / 500 = 1,9.
    farine = ajouter_ingredient(db, "Farine", 2, (300, 10, 70, 1), ["Gluten"])
    lait = ajouter_ingredient(db, "Lait entier", 1, (50, 5, 5, 2.5), ["Lait"])
    plat = Recette(
        titre="Crêpes",
        type=TypePlat.VEGETARIEN,
        vegetarien=True,
        procedure="Mélanger puis cuire.",
        auteur=utilisateur,
        lignes=[
            LigneRecette(ingredient=farine, quantite=200),
            LigneRecette(ingredient=lait, quantite=300),
        ],
    )
    db.add(plat)
    db.commit()
    return plat


def fiche(client, recette):
    return client.get(f"/recettes/{recette.id}/fiche", follow_redirects=False)


def test_TC_S04_11_fiche_affiche_le_contenu_de_la_recette(client_connecte, recette):
    reponse = fiche(client_connecte, recette)

    assert reponse.status_code == 200
    for attendu in ("Crêpes", "Farine", "Lait entier", "Mélanger puis cuire."):
        assert attendu in reponse.text


def test_TC_S04_12_fiche_affiche_le_cout(client_connecte, recette):
    assert "0,70 €" in fiche(client_connecte, recette).text


def test_TC_S04_13_fiche_affiche_la_nutrition_pour_100g(client_connecte, recette):
    texte = fiche(client_connecte, recette).text

    for attendu in ("150,0", "7,0", "31,0", "1,9"):
        assert attendu in texte


def test_TC_S04_14_fiche_affiche_les_allergenes(client_connecte, recette):
    assert "Gluten, Lait" in fiche(client_connecte, recette).text


def test_TC_S04_15_fiche_sans_allergene(client_connecte, db, utilisateur):
    riz = ajouter_ingredient(db, "Riz", 1, (130, 2, 28, 0))
    plat = Recette(
        titre="Riz nature",
        type=TypePlat.FECULENT,
        vegetarien=True,
        procedure="Cuire.",
        auteur=utilisateur,
        lignes=[LigneRecette(ingredient=riz, quantite=100)],
    )
    db.add(plat)
    db.commit()

    assert "Aucun" in fiche(client_connecte, plat).text


def test_TC_S04_16_fiche_inexistante_404(client_connecte):
    assert client_connecte.get("/recettes/999/fiche").status_code == 404


def test_TC_S04_17_fiche_protegee_sans_session(client, recette):
    assert fiche(client, recette).status_code == 303


def test_TC_S04_18_la_liste_mene_a_la_fiche(client_connecte, recette):
    assert f"/recettes/{recette.id}/fiche" in client_connecte.get("/recettes").text
