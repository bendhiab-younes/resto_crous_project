import pytest

from app.models import (
    Allergene,
    Ingredient,
    LigneRecette,
    Recette,
    Role,
    StatutRecette,
    Stock,
    TypePlat,
)


@pytest.fixture
def intendant(client_avec_role):
    return client_avec_role(Role.INTENDANT)


@pytest.fixture
def farine(db):
    ingredient = Ingredient(
        nom="Farine",
        cout_par_kg=2,
        calories=300,
        proteines=10,
        glucides=70,
        lipides=1,
        allergenes=[Allergene(nom="Gluten")],
    )
    db.add(ingredient)
    db.commit()
    return ingredient


@pytest.fixture
def recette(db, utilisateur, farine):
    plat = ajouter_recette(db, utilisateur, farine, "Crêpes", StatutRecette.A_VALIDER)
    return plat


def ajouter_recette(db, auteur, ingredient, titre, statut):
    plat = Recette(
        titre=titre,
        type=TypePlat.VEGETARIEN,
        vegetarien=True,
        procedure="Mélanger.",
        statut=statut,
        auteur=auteur,
        lignes=[LigneRecette(ingredient=ingredient, quantite=200)],
    )
    db.add(plat)
    db.commit()
    return plat


def mettre_en_stock(db, ingredient, quantite):
    db.add(Stock(ingredient=ingredient, quantite_disponible=quantite, seuil_alerte=0))
    db.commit()


def valider(client, recette):
    return client.post(f"/validations/{recette.id}/valider", follow_redirects=False)


def refuser(client, recette, motif="Trop cher"):
    return client.post(
        f"/validations/{recette.id}/refuser", data={"motif": motif}, follow_redirects=False
    )


def statut(db, recette):
    db.refresh(recette)
    return recette.statut


def test_TC_S08_08_liste_des_recettes_a_valider(intendant, db, utilisateur, farine, recette):
    ajouter_recette(db, utilisateur, farine, "Brouillon caché", StatutRecette.BROUILLON)

    reponse = intendant.get("/validations")

    assert reponse.status_code == 200
    assert "Crêpes" in reponse.text
    assert "Brouillon caché" not in reponse.text


def test_TC_S08_09_detail_affiche_les_calculs(intendant, db, farine, recette):
    mettre_en_stock(db, farine, 500)

    texte = intendant.get(f"/validations/{recette.id}").text

    # 200 g à 2 €/kg = 0,40 €.
    assert "0,40 €" in texte
    assert "Gluten" in texte
    assert "300,0" in texte


def test_TC_S08_10_validation_avec_stock_suffisant(intendant, db, farine, recette):
    mettre_en_stock(db, farine, 200)

    reponse = valider(intendant, recette)

    assert reponse.status_code == 303
    assert reponse.headers["location"] == "/validations"
    assert statut(db, recette) is StatutRecette.VALIDEE


def test_TC_S08_11_validation_refusee_si_stock_insuffisant(intendant, db, farine, recette):
    mettre_en_stock(db, farine, 199)

    reponse = valider(intendant, recette)

    assert reponse.status_code == 409
    assert "Farine" in reponse.text
    assert statut(db, recette) is StatutRecette.A_VALIDER


def test_TC_S08_12_validation_refusee_sans_stock_saisi(intendant, db, recette):
    assert valider(intendant, recette).status_code == 409
    assert statut(db, recette) is StatutRecette.A_VALIDER


def test_TC_S08_13_formulaire_de_validation_selon_le_stock(intendant, db, farine, recette):
    action = f"/validations/{recette.id}/valider"
    assert action not in intendant.get(f"/validations/{recette.id}").text

    mettre_en_stock(db, farine, 500)

    assert action in intendant.get(f"/validations/{recette.id}").text


def test_TC_S08_14_refus_avec_motif(intendant, db, recette):
    reponse = refuser(intendant, recette, "  Trop cher  ")

    assert reponse.status_code == 303
    assert reponse.headers["location"] == "/validations"
    assert statut(db, recette) is StatutRecette.REFUSEE
    assert recette.motif_refus == "Trop cher"


def test_TC_S08_15_refus_sans_motif(intendant, db, recette):
    reponse = refuser(intendant, recette, "   ")

    assert reponse.status_code == 422
    assert "Le motif est obligatoire." in reponse.text
    assert statut(db, recette) is StatutRecette.A_VALIDER


def test_TC_S08_16_reserve_a_l_intendant(client_connecte, db, recette):
    assert client_connecte.get("/validations").status_code == 403
    assert client_connecte.get(f"/validations/{recette.id}").status_code == 403
    assert valider(client_connecte, recette).status_code == 403
    assert refuser(client_connecte, recette).status_code == 403
    assert statut(db, recette) is StatutRecette.A_VALIDER


def test_TC_S08_17_sans_session(client, db, recette):
    assert client.get("/validations", follow_redirects=False).status_code == 303
    assert valider(client, recette).status_code == 303
    assert statut(db, recette) is StatutRecette.A_VALIDER


@pytest.mark.parametrize(
    "etat", [StatutRecette.BROUILLON, StatutRecette.VALIDEE, StatutRecette.REFUSEE]
)
def test_TC_S08_18_seule_une_recette_a_valider_est_traitee(intendant, db, recette, etat):
    recette.statut = etat
    db.commit()

    assert intendant.get(f"/validations/{recette.id}").status_code == 404
    assert valider(intendant, recette).status_code == 404
    assert refuser(intendant, recette).status_code == 404
    assert statut(db, recette) is etat


def test_TC_S08_19_recette_inexistante_404(intendant):
    assert intendant.get("/validations/999").status_code == 404


def test_TC_S08_20_motif_affiche_sur_la_fiche(intendant, db, recette):
    refuser(intendant, recette, "Trop cher")

    assert "Trop cher" in intendant.get(f"/recettes/{recette.id}/fiche").text


def test_TC_S08_21_navigation_selon_le_role(client_avec_role):
    texte = client_avec_role(Role.INTENDANT).get("/").text

    assert 'href="/validations"' in texte
    assert 'href="/stocks"' in texte


def test_TC_S08_22_navigation_masquee_pour_le_chef(client_connecte):
    texte = client_connecte.get("/").text

    assert 'href="/validations"' not in texte
    assert 'href="/stocks"' not in texte
