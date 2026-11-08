from sqlalchemy import select

from app.models import SessionUtilisateur

COOKIE = "session"
MESSAGE_ERREUR = "Identifiant ou mot de passe incorrect."


def se_connecter(client, identifiant="chef", mot_de_passe="secret"):
    return client.post(
        "/connexion",
        data={"identifiant": identifiant, "mot_de_passe": mot_de_passe},
        follow_redirects=False,
    )


def test_TC_S01_05_page_de_connexion_affichee(client):
    assert client.get("/connexion").status_code == 200


def test_TC_S01_06_connexion_valide_ouvre_une_session(client, utilisateur, db):
    reponse = se_connecter(client)

    assert reponse.status_code == 303
    assert reponse.headers["location"] == "/"
    assert COOKIE in client.cookies
    assert db.scalar(select(SessionUtilisateur)).utilisateur_id == utilisateur.id


def test_TC_S01_07_cookie_de_session_inaccessible_au_javascript(client, utilisateur):
    assert "httponly" in se_connecter(client).headers["set-cookie"].lower()


def test_TC_S01_08_mauvais_mot_de_passe_refuse(client, utilisateur):
    reponse = se_connecter(client, mot_de_passe="faux")

    assert reponse.status_code == 401
    assert MESSAGE_ERREUR in reponse.text
    assert COOKIE not in client.cookies


def test_TC_S01_09_compte_inconnu_meme_reponse(client, utilisateur):
    mauvais_mot_de_passe = se_connecter(client, mot_de_passe="faux")
    compte_inconnu = se_connecter(client, identifiant="inconnu", mot_de_passe="faux")

    assert compte_inconnu.status_code == mauvais_mot_de_passe.status_code
    assert compte_inconnu.text == mauvais_mot_de_passe.text


def test_TC_S01_13_deconnexion_efface_le_cookie(client_connecte):
    reponse = client_connecte.post("/deconnexion", follow_redirects=False)

    assert reponse.status_code == 303
    assert reponse.headers["location"] == "/connexion"
    assert COOKIE not in client_connecte.cookies
