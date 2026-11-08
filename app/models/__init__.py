"""Modèles SQLAlchemy : chaque modèle est importé ici pour que `init_db` crée sa table."""

from app.models.ingredient import Allergene, Ingredient
from app.models.utilisateur import Role, SessionUtilisateur, Utilisateur

__all__ = ["Allergene", "Ingredient", "Role", "SessionUtilisateur", "Utilisateur"]
