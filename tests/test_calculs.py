from types import SimpleNamespace

import pytest

from app.calculs import (
    allergenes_recette,
    cout_recette,
    ingredients_manquants,
    nutrition_pour_100g,
)


def ingredient(cout_par_kg=0.0, calories=0.0, proteines=0.0, glucides=0.0, lipides=0.0, allergenes=()):
    return SimpleNamespace(
        cout_par_kg=cout_par_kg,
        calories=calories,
        proteines=proteines,
        glucides=glucides,
        lipides=lipides,
        allergenes=[SimpleNamespace(nom=nom) for nom in allergenes],
    )


def ligne(quantite, ingredient):
    return SimpleNamespace(quantite=quantite, ingredient=ingredient)


def test_TC_S04_01_cout_une_ligne():
    # 250 g à 8 €/kg : 0,25 × 8 = 2 €
    assert cout_recette([ligne(250, ingredient(cout_par_kg=8))]) == pytest.approx(2.0)


def test_TC_S04_02_cout_somme_des_lignes():
    # 500 g à 2 €/kg = 1 € ; 200 g à 10 €/kg = 2 € ; total 3 €
    lignes = [ligne(500, ingredient(cout_par_kg=2)), ligne(200, ingredient(cout_par_kg=10))]
    assert cout_recette(lignes) == pytest.approx(3.0)


def test_TC_S04_03_cout_liste_vide_vaut_zero():
    resultat = cout_recette([])
    assert resultat == 0
    assert isinstance(resultat, float)


def test_TC_S04_04_nutrition_une_ligne_garde_les_valeurs_de_l_ingredient():
    riz = ingredient(calories=130, proteines=2, glucides=28, lipides=0.5)
    assert nutrition_pour_100g([ligne(300, riz)]) == pytest.approx(
        {"calories": 130, "proteines": 2, "glucides": 28, "lipides": 0.5}
    )


def test_TC_S04_05_nutrition_moyenne_ponderee_par_la_quantite():
    # Total 400 g.
    # calories : (300 × 130 + 100 × 170) / 400 = 56000 / 400 = 140
    # protéines : (300 × 2 + 100 × 30) / 400 = 3600 / 400 = 9
    # glucides : (300 × 28 + 100 × 0) / 400 = 8400 / 400 = 21
    # lipides : (300 × 0 + 100 × 6) / 400 = 600 / 400 = 1,5
    riz = ingredient(calories=130, proteines=2, glucides=28, lipides=0)
    poulet = ingredient(calories=170, proteines=30, glucides=0, lipides=6)
    assert nutrition_pour_100g([ligne(300, riz), ligne(100, poulet)]) == pytest.approx(
        {"calories": 140, "proteines": 9, "glucides": 21, "lipides": 1.5}
    )


def test_TC_S04_06_nutrition_liste_vide_refusee():
    with pytest.raises(ValueError):
        nutrition_pour_100g([])


def test_TC_S04_07_nutrition_quantite_totale_nulle_refusee():
    with pytest.raises(ValueError):
        nutrition_pour_100g([ligne(0, ingredient(calories=130)), ligne(0, ingredient(calories=170))])


def test_TC_S04_08_allergenes_union_triee_sans_doublon():
    lignes = [
        ligne(100, ingredient(allergenes=["lait", "gluten"])),
        ligne(50, ingredient(allergenes=["oeuf", "gluten"])),
    ]
    assert allergenes_recette(lignes) == ["gluten", "lait", "oeuf"]


def test_TC_S04_09_allergenes_ingredients_sans_allergene():
    assert allergenes_recette([ligne(100, ingredient())]) == []


def test_TC_S04_10_allergenes_liste_vide():
    assert allergenes_recette([]) == []


def ligne_stock(ingredient_id, nom, quantite):
    return SimpleNamespace(
        quantite=quantite, ingredient=SimpleNamespace(id=ingredient_id, nom=nom)
    )


def test_TC_S08_01_stock_suffisant():
    assert ingredients_manquants([ligne_stock(1, "Farine", 200)], {1: 500}) == []


def test_TC_S08_02_stock_exactement_egal_au_besoin():
    assert ingredients_manquants([ligne_stock(1, "Farine", 200)], {1: 200}) == []


def test_TC_S08_03_stock_insuffisant():
    assert ingredients_manquants([ligne_stock(1, "Farine", 200)], {1: 199.5}) == ["Farine"]


def test_TC_S08_04_ingredient_absent_du_stock():
    assert ingredients_manquants([ligne_stock(1, "Farine", 1)], {}) == ["Farine"]


def test_TC_S08_05_quantites_additionnees_sur_plusieurs_lignes():
    lignes = [ligne_stock(1, "Farine", 200), ligne_stock(1, "Farine", 150)]

    # Besoin total 350 g : 300 g ne suffisent pas, 350 g suffisent.
    assert ingredients_manquants(lignes, {1: 300}) == ["Farine"]
    assert ingredients_manquants(lignes, {1: 350}) == []


def test_TC_S08_06_manquants_tries_sans_doublon():
    lignes = [
        ligne_stock(2, "Sel", 10),
        ligne_stock(1, "Farine", 200),
        ligne_stock(2, "Sel", 10),
        ligne_stock(3, "Eau", 100),
    ]

    assert ingredients_manquants(lignes, {3: 100}) == ["Farine", "Sel"]


def test_TC_S08_07_liste_vide_aucun_manquant():
    assert ingredients_manquants([], {1: 10}) == []
