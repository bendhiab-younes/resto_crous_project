import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.database import IN_MEMORY_URL, create_db_engine, get_db, init_db
from app.main import app


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
