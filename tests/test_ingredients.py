import pytest
from sqlalchemy import select

from app.donnees_initiales import ALLERGENES_REGLEMENTAIRES, charger_allergenes
from app.models import Allergene, Ingredient

DONNEES = {
    "nom": "Tomate",
    "cout_par_kg": "2.5",
    "calories": "18",
    "proteines": "0.9",
    "glucides": "3.9",
    "lipides": "0.2",
}


def creer(db, nom="Farine", allergenes=()):
    ingredient = Ingredient(
        nom=nom,
        cout_par_kg=1.2,
        calories=364,
        proteines=10,
        glucides=76,
        lipides=1,
        allergenes=list(allergenes),
    )
    db.add(ingredient)
    db.commit()
    return ingredient


def allergene(db, nom="Gluten"):
    resultat = Allergene(nom=nom)
    db.add(resultat)
    db.commit()
    return resultat


def poster(client, url="/ingredients", **champs):
    return client.post(url, data=DONNEES | champs, follow_redirects=False)


def noms(db):
    return db.scalars(select(Ingredient.nom)).all()


def test_TC_S02_01_creation_d_un_ingredient(client_connecte, db):
    gluten = allergene(db)

    reponse = poster(client_connecte, allergenes=[str(gluten.id)])

    assert reponse.status_code == 303
    assert reponse.headers["location"] == "/ingredients"
    ingredient = db.scalar(select(Ingredient))
    assert ingredient.nom == "Tomate"
    assert ingredient.cout_par_kg == 2.5
    assert (ingredient.calories, ingredient.proteines) == (18, 0.9)
    assert (ingredient.glucides, ingredient.lipides) == (3.9, 0.2)
    assert [a.nom for a in ingredient.allergenes] == ["Gluten"]


def test_TC_S02_02_nom_obligatoire(client_connecte, db):
    reponse = poster(client_connecte, nom="   ")

    assert reponse.status_code == 422
    assert "Le nom est obligatoire." in reponse.text
    assert noms(db) == []


def test_TC_S02_03_cout_negatif_refuse(client_connecte, db):
    reponse = poster(client_connecte, cout_par_kg="-1")

    assert reponse.status_code == 422
    assert "Le coût ne peut pas être négatif." in reponse.text
    assert noms(db) == []


def test_TC_S02_04_nom_unique(client_connecte, db):
    creer(db, nom="Tomate")

    reponse = poster(client_connecte, nom=" tomate ")

    assert reponse.status_code == 422
    assert "Un ingrédient porte déjà ce nom." in reponse.text
    assert noms(db) == ["Tomate"]


def test_TC_S02_05_valeur_non_numerique_affichee_a_l_utilisateur(client_connecte, db):
    reponse = poster(client_connecte, calories="beaucoup")

    assert reponse.status_code == 422
    assert "text/html" in reponse.headers["content-type"]
    assert "Saisir un nombre." in reponse.text
    assert noms(db) == []


def test_TC_S02_06_valeur_non_finie_refusee(client_connecte, db):
    assert poster(client_connecte, cout_par_kg="nan").status_code == 422
    assert poster(client_connecte, calories="inf").status_code == 422
    assert noms(db) == []


def test_TC_S02_07_virgule_decimale_acceptee(client_connecte, db):
    poster(client_connecte, cout_par_kg="2,5")

    assert db.scalar(select(Ingredient)).cout_par_kg == 2.5


def test_TC_S02_08_allergene_inconnu_refuse(client_connecte, db):
    reponse = poster(client_connecte, allergenes=["999"])

    assert reponse.status_code == 422
    assert noms(db) == []


def test_TC_S02_09_saisie_conservee_apres_une_erreur(client_connecte):
    reponse = poster(client_connecte, nom="Basilic", cout_par_kg="-1")

    assert "Basilic" in reponse.text


def test_TC_S02_10_liste_des_ingredients(client_connecte, db):
    creer(db, nom="Farine", allergenes=[allergene(db)])

    reponse = client_connecte.get("/ingredients")

    assert reponse.status_code == 200
    assert "Farine" in reponse.text
    assert "Gluten" in reponse.text


def test_TC_S02_11_formulaire_de_creation(client_connecte, db):
    allergene(db, "Arachides")

    reponse = client_connecte.get("/ingredients/nouveau")

    assert reponse.status_code == 200
    assert "Arachides" in reponse.text


def test_TC_S02_12_formulaire_de_modification_prerempli(client_connecte, db):
    ingredient = creer(db, nom="Farine")

    reponse = client_connecte.get(f"/ingredients/{ingredient.id}")

    assert reponse.status_code == 200
    assert "Farine" in reponse.text


def test_TC_S02_13_modification(client_connecte, db):
    ingredient = creer(db, nom="Farine", allergenes=[allergene(db)])

    reponse = poster(client_connecte, f"/ingredients/{ingredient.id}", nom="Farine T55")

    assert reponse.status_code == 303
    db.refresh(ingredient)
    assert ingredient.nom == "Farine T55"
    assert ingredient.cout_par_kg == 2.5
    assert ingredient.allergenes == []


def test_TC_S02_14_modification_sans_changer_le_nom(client_connecte, db):
    ingredient = creer(db, nom="Tomate")

    assert poster(client_connecte, f"/ingredients/{ingredient.id}").status_code == 303


def test_TC_S02_15_modification_vers_un_nom_pris_refusee(client_connecte, db):
    creer(db, nom="Tomate")
    ingredient = creer(db, nom="Farine")

    reponse = poster(client_connecte, f"/ingredients/{ingredient.id}", nom="Tomate")

    assert reponse.status_code == 422
    db.refresh(ingredient)
    assert ingredient.nom == "Farine"


def test_TC_S02_16_suppression(client_connecte, db):
    ingredient = creer(db)

    reponse = client_connecte.post(
        f"/ingredients/{ingredient.id}/supprimer", follow_redirects=False
    )

    assert reponse.status_code == 303
    assert noms(db) == []


def test_TC_S02_17_ingredient_inexistant_404(client_connecte):
    assert client_connecte.get("/ingredients/999").status_code == 404
    assert poster(client_connecte, "/ingredients/999").status_code == 404
    assert client_connecte.post("/ingredients/999/supprimer").status_code == 404


def test_TC_S02_18_ecriture_refusee_sans_session(client, db):
    assert poster(client).status_code == 303
    assert noms(db) == []


def test_TC_S02_19_allergenes_reglementaires_charges_une_seule_fois(db):
    charger_allergenes(db)
    charger_allergenes(db)

    assert len(db.scalars(select(Allergene.nom)).all()) == len(ALLERGENES_REGLEMENTAIRES)


def test_TC_S02_20_cout_negatif_refuse_en_modification(client_connecte, db):
    ingredient = creer(db, nom="Farine")

    reponse = poster(client_connecte, f"/ingredients/{ingredient.id}", cout_par_kg="-1")

    assert reponse.status_code == 422
    assert "Le coût ne peut pas être négatif." in reponse.text
    db.refresh(ingredient)
    assert ingredient.cout_par_kg == 1.2


def test_TC_S02_21_nom_vide_refuse_en_modification(client_connecte, db):
    ingredient = creer(db, nom="Farine")

    reponse = poster(client_connecte, f"/ingredients/{ingredient.id}", nom="  ")

    assert reponse.status_code == 422
    assert "Le nom est obligatoire." in reponse.text
    db.refresh(ingredient)
    assert ingredient.nom == "Farine"


@pytest.mark.parametrize("champ", ["calories", "proteines", "glucides", "lipides"])
def test_TC_S02_22_valeur_nutritionnelle_negative_refusee(client_connecte, db, champ):
    reponse = poster(client_connecte, **{champ: "-1"})

    assert reponse.status_code == 422
    assert "La valeur ne peut pas être négative." in reponse.text
    assert noms(db) == []


def test_TC_S02_23_modification_des_allergenes(client_connecte, db):
    gluten = allergene(db, "Gluten")
    lait = allergene(db, "Lait")
    ingredient = creer(db, nom="Farine", allergenes=[gluten])

    reponse = poster(client_connecte, f"/ingredients/{ingredient.id}", allergenes=[str(lait.id)])

    assert reponse.status_code == 303
    db.refresh(ingredient)
    assert [a.nom for a in ingredient.allergenes] == ["Lait"]
