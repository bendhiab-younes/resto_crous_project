from sqlalchemy import CheckConstraint, Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

ingredient_allergene = Table(
    "ingredient_allergene",
    Base.metadata,
    Column("ingredient_id", ForeignKey("ingredients.id", ondelete="CASCADE"), primary_key=True),
    Column("allergene_id", ForeignKey("allergenes.id", ondelete="CASCADE"), primary_key=True),
)


class Allergene(Base):
    __tablename__ = "allergenes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(unique=True)


class Ingredient(Base):
    """Coût au kilo, valeurs nutritionnelles pour 100 g."""

    __tablename__ = "ingredients"
    __table_args__ = (CheckConstraint("cout_par_kg >= 0", name="cout_par_kg_positif"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(unique=True)
    cout_par_kg: Mapped[float]
    calories: Mapped[float]
    proteines: Mapped[float]
    glucides: Mapped[float]
    lipides: Mapped[float]
    allergenes: Mapped[list[Allergene]] = relationship(
        secondary=ingredient_allergene, order_by=Allergene.nom
    )
