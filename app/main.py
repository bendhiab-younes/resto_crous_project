from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app import models  # noqa: F401
from app.database import SessionLocal, init_db
from app.donnees_initiales import charger_allergenes
from app.routers import connexion, ingredients, pages, recettes


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
    init_db()
    with SessionLocal() as session:
        charger_allergenes(session)
    yield


app = FastAPI(title="Gestionnaire de menus et de recettes", lifespan=lifespan)
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")
app.include_router(pages.router)
app.include_router(connexion.router)
app.include_router(ingredients.router)
app.include_router(recettes.router)
