import os
from collections.abc import Iterator
from pathlib import Path

from sqlalchemy import Engine, create_engine, event
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from sqlalchemy.pool import StaticPool

DEFAULT_DATABASE_URL = f"sqlite:///{Path(__file__).resolve().parent.parent / 'resto.db'}"
IN_MEMORY_URL = "sqlite://"


class Base(DeclarativeBase):
    pass


def create_db_engine(url: str) -> Engine:
    options = {"connect_args": {"check_same_thread": False}}
    if url == IN_MEMORY_URL:
        # Une base en mémoire disparaît avec sa connexion : on en garde une seule.
        options["poolclass"] = StaticPool
    engine = create_engine(url, **options)

    # SQLite n'applique pas les clés étrangères par défaut.
    @event.listens_for(engine, "connect")
    def enable_foreign_keys(connection, _record):
        connection.execute("PRAGMA foreign_keys=ON")

    return engine


engine = create_db_engine(os.environ.get("DATABASE_URL", DEFAULT_DATABASE_URL))
SessionLocal = sessionmaker(bind=engine)


def init_db(bind: Engine = engine) -> None:
    Base.metadata.create_all(bind)


def get_db() -> Iterator[Session]:
    with SessionLocal() as session:
        yield session
