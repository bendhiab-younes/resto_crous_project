"""Change le rôle d'un compte : python -m app.changer_role <identifiant> <CHEF|INTENDANT|GESTION_CENTRALE>"""

import argparse

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import SessionLocal, init_db
from app.models import Role, Utilisateur


def changer_role(db: Session, identifiant: str, role: Role) -> None:
    utilisateur = db.scalar(select(Utilisateur).where(Utilisateur.identifiant == identifiant))
    if utilisateur is None:
        raise ValueError(f"le compte {identifiant} n'existe pas")
    utilisateur.role = role
    db.commit()


def main() -> None:
    parser = argparse.ArgumentParser(description="Change le rôle d'un compte.")
    parser.add_argument("identifiant")
    parser.add_argument("role", type=Role, choices=list(Role))
    args = parser.parse_args()

    init_db()
    with SessionLocal() as session:
        try:
            changer_role(session, args.identifiant, args.role)
        except ValueError as erreur:
            parser.error(str(erreur))
    print(f"Le compte {args.identifiant} a maintenant le rôle {args.role}.")


if __name__ == "__main__":
    main()
