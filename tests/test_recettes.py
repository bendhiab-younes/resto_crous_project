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
