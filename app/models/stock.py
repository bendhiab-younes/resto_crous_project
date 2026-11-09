from sqlalchemy import CheckConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.ingredient import Ingredient


class Stock(Base):
    __tablename__ = "stocks"
    __table_args__ = (
        CheckConstraint("quantite_disponible >= 0", name="quantite_disponible_positive"),
        CheckConstraint("seuil_alerte >= 0", name="seuil_alerte_positive"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    ingredient_id: Mapped[int] = mapped_column(
        ForeignKey("ingredients.id", ondelete="CASCADE"), unique=True
    )
    quantite_disponible: Mapped[float]
    seuil_alerte: Mapped[float]
    ingredient: Mapped[Ingredient] = relationship()

    def est_suffisant_pour(self, quantite: float) -> bool:
        return self.quantite_disponible >= quantite
