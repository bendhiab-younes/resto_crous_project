import pytest
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.models import Ingredient, LigneRecette, Recette, StatutRecette, TypePlat


@pytest.fixture
def farine(db):
    return ajouter_ingredient(db, "Farine")


@pytest.fixture
def lait(db):
    return ajouter_ingredient(db, "Lait")


def ajouter_ingredient(db, nom):
    ingredient = Ingredient(
        nom=nom, cout_par_kg=1, calories=100, proteines=1, glucides=1, lipides=1
    )
    db.add(ingredient)
    db.commit()
    return ingredient


def ajouter_recette(db, auteur, ingredient, titre="Crêpes"):
    recette = Recette(
        titre=titre,
        type=TypePlat.VEGETARIEN,
        vegetarien=True,
        procedure="Mélanger.",
        auteur=auteur,
        lignes=[LigneRecette(ingredient=ingredient, quantite=250)],
    )
    db.add(recette)
    db.commit()
    return recette


def poster(client, ingredient, url="/recettes", **champs):
    donnees = {
        "titre": "Purée",
        "type": "LEGUME",
        "vegetarien": "on",
        "procedure": "Écraser.",
        "ingredient_id": [str(ingredient.id)],
        "quantite": ["500"],
    }
    return client.post(url, data=donnees | champs, follow_redirects=False)


def recettes(db):
    return db.scalars(select(Recette)).all()


def test_TC_S03_01_recette_creee_en_brouillon(db, utilisateur, farine):
    recette = ajouter_recette(db, utilisateur, farine)

    assert recette.statut is StatutRecette.BROUILLON
    assert recette.lignes[0].quantite == 250
    assert recette.lignes[0].ingredient is farine


def test_TC_S03_02_supprimer_la_recette_supprime_ses_lignes(db, utilisateur, farine):
    db.delete(ajouter_recette(db, utilisateur, farine))
    db.commit()

    assert db.scalars(select(LigneRecette)).all() == []
    assert db.get(Ingredient, farine.id) is farine


def test_TC_S03_03_ingredient_d_une_recette_protege_en_base(db, utilisateur, farine):
    ajouter_recette(db, utilisateur, farine)

    db.delete(farine)
    with pytest.raises(IntegrityError):
        db.commit()


def test_TC_S03_04_creation_par_formulaire(client_connecte, db, utilisateur, farine, lait):
    reponse = poster(
        client_connecte,
        farine,
        ingredient_id=[str(farine.id), str(lait.id)],
        quantite=["500", "1,5"],
    )

    assert reponse.status_code == 303
    assert reponse.headers["location"] == "/recettes"
    recette = db.scalar(select(Recette))
    assert (recette.titre, recette.type, recette.vegetarien) == ("Purée", TypePlat.LEGUME, True)
    assert recette.procedure == "Écraser."
    assert recette.statut is StatutRecette.BROUILLON
    assert recette.auteur is utilisateur
    assert [(l.ingredient.nom, l.quantite) for l in recette.lignes] == [
        ("Farine", 500),
        ("Lait", 1.5),
    ]


def test_TC_S03_05_case_vegetarien_decochee(client_connecte, db, farine):
    donnees = {
        "titre": "Purée",
        "type": "LEGUME",
        "procedure": "Écraser.",
        "ingredient_id": [str(farine.id)],
        "quantite": ["500"],
    }

    client_connecte.post("/recettes", data=donnees)

    assert db.scalar(select(Recette)).vegetarien is False


def test_TC_S03_06_lignes_vides_ignorees(client_connecte, db, farine):
    reponse = poster(
        client_connecte, farine, ingredient_id=[str(farine.id), ""], quantite=["500", ""]
    )

    assert reponse.status_code == 303
    assert len(db.scalar(select(Recette)).lignes) == 1


@pytest.mark.parametrize(
    ("champs", "message"),
    [
        ({"titre": "  "}, "Le titre est obligatoire."),
        ({"type": "DESSERT"}, "Type de plat inconnu."),
        ({"procedure": ""}, "La procédure est obligatoire."),
        ({"ingredient_id": [""], "quantite": [""]}, "Ajouter au moins un ingrédient."),
        ({"quantite": ["0"]}, "La quantité doit être un nombre positif, en grammes."),
        ({"quantite": ["-5"]}, "La quantité doit être un nombre positif, en grammes."),
        ({"quantite": ["beaucoup"]}, "La quantité doit être un nombre positif, en grammes."),
        ({"quantite": []}, "La quantité doit être un nombre positif, en grammes."),
        ({"ingredient_id": ["999"]}, "Ingrédient inconnu."),
    ],
)
def test_TC_S03_07_saisie_invalide_refusee(client_connecte, db, farine, champs, message):
    reponse = poster(client_connecte, farine, **champs)

    assert reponse.status_code == 422
    assert message in reponse.text
    assert recettes(db) == []


def test_TC_S03_08_saisie_conservee_apres_une_erreur(client_connecte, farine):
    reponse = poster(client_connecte, farine, titre="Gratin", quantite=["-5"])

    assert "Gratin" in reponse.text


def test_TC_S03_09_liste_des_recettes(client_connecte, db, utilisateur, farine):
    ajouter_recette(db, utilisateur, farine, titre="Crêpes")

    reponse = client_connecte.get("/recettes")

    assert reponse.status_code == 200
    assert "Crêpes" in reponse.text


def test_TC_S03_10_formulaire_de_creation(client_connecte, farine):
    reponse = client_connecte.get("/recettes/nouveau")

    assert reponse.status_code == 200
    assert "Farine" in reponse.text


def test_TC_S03_11_formulaire_de_modification_prerempli(client_connecte, db, utilisateur, farine):
    recette = ajouter_recette(db, utilisateur, farine, titre="Crêpes")

    reponse = client_connecte.get(f"/recettes/{recette.id}")

    assert reponse.status_code == 200
    assert "Crêpes" in reponse.text


def test_TC_S03_12_modification_remplace_les_lignes(client_connecte, db, utilisateur, farine, lait):
    recette = ajouter_recette(db, utilisateur, farine)

    reponse = poster(client_connecte, lait, f"/recettes/{recette.id}", titre="Béchamel")

    assert reponse.status_code == 303
    db.refresh(recette)
    assert recette.titre == "Béchamel"
    assert [(l.ingredient.nom, l.quantite) for l in recette.lignes] == [("Lait", 500)]
    assert len(db.scalars(select(LigneRecette)).all()) == 1


def test_TC_S03_13_modification_invalide_sans_effet(client_connecte, db, utilisateur, farine):
    recette = ajouter_recette(db, utilisateur, farine, titre="Crêpes")

    reponse = poster(client_connecte, farine, f"/recettes/{recette.id}", titre="")

    assert reponse.status_code == 422
    db.refresh(recette)
    assert recette.titre == "Crêpes"


def test_TC_S03_14_suppression(client_connecte, db, utilisateur, farine):
    recette = ajouter_recette(db, utilisateur, farine)

    reponse = client_connecte.post(f"/recettes/{recette.id}/supprimer", follow_redirects=False)

    assert reponse.status_code == 303
    assert recettes(db) == []


def test_TC_S03_15_recette_inexistante_404(client_connecte, farine):
    assert client_connecte.get("/recettes/999").status_code == 404
    assert poster(client_connecte, farine, "/recettes/999").status_code == 404
    assert client_connecte.post("/recettes/999/supprimer").status_code == 404


def test_TC_S03_16_pages_protegees(client, db, farine):
    assert client.get("/recettes", follow_redirects=False).status_code == 303
    assert poster(client, farine).status_code == 303
    assert recettes(db) == []


def test_TC_S03_17_suppression_d_un_ingredient_utilise_refusee(
    client_connecte, db, utilisateur, farine
):
    ajouter_recette(db, utilisateur, farine)

    reponse = client_connecte.post(f"/ingredients/{farine.id}/supprimer")

    assert reponse.status_code == 409
    assert "utilisé dans une recette" in reponse.text
    assert db.get(Ingredient, farine.id) is not None


def test_TC_S03_18_modification_sans_ingredient_refusee(client_connecte, db, utilisateur, farine):
    recette = ajouter_recette(db, utilisateur, farine, titre="Crêpes")

    reponse = poster(
        client_connecte, farine, f"/recettes/{recette.id}", ingredient_id=[""], quantite=[""]
    )

    assert reponse.status_code == 422
    assert "Ajouter au moins un ingrédient." in reponse.text
    db.refresh(recette)
    assert [(l.ingredient.nom, l.quantite) for l in recette.lignes] == [("Farine", 250)]


@pytest.mark.parametrize("type_plat", list(TypePlat))
def test_TC_S03_19_chaque_type_de_plat_accepte(client_connecte, db, farine, type_plat):
    reponse = poster(client_connecte, farine, type=type_plat.value)

    assert reponse.status_code == 303
    assert db.scalar(select(Recette)).type is type_plat
