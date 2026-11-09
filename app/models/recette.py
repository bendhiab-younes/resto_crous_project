import enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.ingredient import Ingredient
from app.models.utilisateur import Utilisateur


class TypePlat(enum.StrEnum):
    PROTEINE = "PROTEINE"
    FECULENT = "FECULENT"
    LEGUME = "LEGUME"
    VEGETARIEN = "VEGETARIEN"


class StatutRecette(enum.StrEnum):
    BROUILLON = "BROUILLON"
    A_VALIDER = "A_VALIDER"
    VALIDEE = "VALIDEE"
    REFUSEE = "REFUSEE"


class Recette(Base):
    __tablename__ = "recettes"

    id: Mapped[int] = mapped_column(primary_key=True)
    titre: Mapped[str]
    type: Mapped[TypePlat]
    vegetarien: Mapped[bool]
    procedure: Mapped[str]
    statut: Mapped[StatutRecette] = mapped_column(default=StatutRecette.BROUILLON)
    motif_refus: Mapped[str | None]
    auteur_id: Mapped[int] = mapped_column(ForeignKey("utilisateurs.id"))
    auteur: Mapped[Utilisateur] = relationship()
    lignes: Mapped[list["LigneRecette"]] = relationship(
        cascade="all, delete-orphan", order_by="LigneRecette.id"
    )


class LigneRecette(Base):
    """Quantité d'un ingrédient dans une recette, en grammes."""

    __tablename__ = "lignes_recette"

    id: Mapped[int] = mapped_column(primary_key=True)
    recette_id: Mapped[int] = mapped_column(ForeignKey("recettes.id", ondelete="CASCADE"))
    ingredient_id: Mapped[int] = mapped_column(ForeignKey("ingredients.id", ondelete="RESTRICT"))
    quantite: Mapped[float]
    ingredient: Mapped[Ingredient] = relationship()
