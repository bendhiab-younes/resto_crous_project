import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.database import IN_MEMORY_URL, create_db_engine, get_db, init_db
from app.main import app
from app.models import Role, Utilisateur


@pytest.fixture
def db():
    engine = create_db_engine(IN_MEMORY_URL)
    init_db(engine)
    with Session(engine) as session:
        yield session
    engine.dispose()


@pytest.fixture
def client(db):
    app.dependency_overrides[get_db] = lambda: db
    yield TestClient(app)
    app.dependency_overrides.clear()


@pytest.fixture
def utilisateur(db):
    compte = Utilisateur(identifiant="chef", role=Role.CHEF)
    compte.definir_mot_de_passe("secret")
    db.add(compte)
    db.commit()
    return compte


@pytest.fixture
def client_connecte(client, utilisateur):
    client.post("/connexion", data={"identifiant": "chef", "mot_de_passe": "secret"})
    return client


@pytest.fixture
def client_avec_role(client, db):
    def connecter(role):
        identifiant = role.value.lower()
        compte = Utilisateur(identifiant=identifiant, role=role)
        compte.definir_mot_de_passe("secret")
        db.add(compte)
        db.commit()
        client.post("/connexion", data={"identifiant": identifiant, "mot_de_passe": "secret"})
        return client

    return connecter
