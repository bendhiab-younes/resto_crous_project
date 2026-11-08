import enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.securite import hacher_mot_de_passe, verifier_mot_de_passe


class Role(enum.StrEnum):
    CHEF = "CHEF"
    INTENDANT = "INTENDANT"
    GESTION_CENTRALE = "GESTION_CENTRALE"


class Utilisateur(Base):
    __tablename__ = "utilisateurs"

    id: Mapped[int] = mapped_column(primary_key=True)
    identifiant: Mapped[str] = mapped_column(unique=True)
    mot_de_passe_hache: Mapped[str]
    role: Mapped[Role]

    def definir_mot_de_passe(self, mot_de_passe: str) -> None:
        self.mot_de_passe_hache = hacher_mot_de_passe(mot_de_passe)

    def verifier_mot_de_passe(self, mot_de_passe: str) -> bool:
        return verifier_mot_de_passe(mot_de_passe, self.mot_de_passe_hache)


class SessionUtilisateur(Base):
    """Session côté serveur : supprimer la ligne invalide le cookie, même s'il a été copié."""

    __tablename__ = "sessions_utilisateurs"

    jeton: Mapped[str] = mapped_column(primary_key=True)
    utilisateur_id: Mapped[int] = mapped_column(ForeignKey("utilisateurs.id", ondelete="CASCADE"))
    utilisateur: Mapped[Utilisateur] = relationship()
