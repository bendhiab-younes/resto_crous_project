def test_TC_T22_03_page_d_accueil_affichee(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Gestionnaire de menus et de recettes" in response.text


def test_TC_T22_04_page_d_accueil_charge_la_feuille_de_style(client):
    assert "/static/style.css" in client.get("/").text
    assert client.get("/static/style.css").status_code == 200


def test_TC_T22_05_sante_verifie_la_base(client):
    response = client.get("/sante")

    assert response.status_code == 200
    assert response.json() == {"statut": "ok"}


def test_TC_T22_06_route_inconnue_renvoie_404(client):
    assert client.get("/route-inconnue").status_code == 404
