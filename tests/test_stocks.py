from sqlalchemy import select

from app.models import Ingredient, Role, Stock


def ajouter_ingredient(db, nom="Farine"):
    ingredient = Ingredient(
        nom=nom, cout_par_kg=1, calories=100, proteines=1, glucides=1, lipides=1
    )
    db.add(ingredient)
    db.commit()
    return ingredient


def test_TC_S07_01_intendant_saisit_et_modifie_un_stock(client_avec_role, db):
    client = client_avec_role(Role.INTENDANT)
    ingredient = ajouter_ingredient(db)

    reponse = client.post(
        f"/stocks/{ingredient.id}",
        data={"quantite_disponible": "1200", "seuil_alerte": "300"},
        follow_redirects=False,
    )

    assert reponse.status_code == 303
    stock = db.scalar(select(Stock))
    assert (stock.quantite_disponible, stock.seuil_alerte) == (1200, 300)
    assert stock.est_suffisant_pour(1000)
    assert not stock.est_suffisant_pour(1500)


def test_TC_S07_02_valeur_negative_refusee(client_avec_role, db):
    client = client_avec_role(Role.INTENDANT)
    ingredient = ajouter_ingredient(db)

    reponse = client.post(
        f"/stocks/{ingredient.id}",
        data={"quantite_disponible": "-1", "seuil_alerte": "300"},
    )

    assert reponse.status_code == 422
    assert "La valeur ne peut pas être négative." in reponse.text
    assert db.scalar(select(Stock)) is None


def test_TC_S07_03_autre_role_interdit(client_avec_role, db):
    client = client_avec_role(Role.CHEF)
    ingredient = ajouter_ingredient(db)

    assert client.get("/stocks").status_code == 403
    assert client.get(f"/stocks/{ingredient.id}").status_code == 403


def test_TC_S07_04_valeur_non_numerique_refusee(client_avec_role, db):
    client = client_avec_role(Role.INTENDANT)
    ingredient = ajouter_ingredient(db)

    reponse = client.post(
        f"/stocks/{ingredient.id}",
        data={"quantite_disponible": "beaucoup", "seuil_alerte": "300"},
    )

    assert reponse.status_code == 422
    assert "Saisir un nombre." in reponse.text
    assert db.scalar(select(Stock)) is None
