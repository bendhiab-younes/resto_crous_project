from sqlalchemy import Column, Integer, Table, inspect, text

from app.database import Base, create_db_engine, init_db


def test_TC_T22_01_cles_etrangeres_actives():
    engine = create_db_engine("sqlite://")
    with engine.connect() as connection:
        assert connection.execute(text("PRAGMA foreign_keys")).scalar() == 1


def test_TC_T22_02_init_db_cree_les_tables_declarees():
    engine = create_db_engine("sqlite://")
    table = Table("table_de_test", Base.metadata, Column("id", Integer, primary_key=True))
    try:
        init_db(engine)
        assert inspect(engine).has_table("table_de_test")
    finally:
        Base.metadata.remove(table)
