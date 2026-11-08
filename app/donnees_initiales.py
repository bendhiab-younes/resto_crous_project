from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Allergene

# Les 14 allergènes à déclaration obligatoire (règlement UE INCO n° 1169/2011).
ALLERGENES_REGLEMENTAIRES = (
    "Arachides",
    "Céleri",
    "Crustacés",
    "Fruits à coque",
    "Gluten",
    "Lait",
    "Lupin",
    "Mollusques",
    "Moutarde",
    "Œufs",
    "Poissons",
    "Sésame",
    "Soja",
    "Sulfites",
)


def charger_allergenes(db: Session) -> None:
    existants = set(db.scalars(select(Allergene.nom)))
    db.add_all(Allergene(nom=nom) for nom in ALLERGENES_REGLEMENTAIRES if nom not in existants)
    db.commit()
