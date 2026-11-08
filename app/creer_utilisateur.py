"""Crée un compte : python -m app.creer_utilisateur <identifiant> <CHEF|INTENDANT|GESTION_CENTRALE>"""

import argparse
import getpass

from sqlalchemy import select

from app.database import SessionLocal, init_db
from app.models import Role, Utilisateur


def main() -> None:
    parser = argparse.ArgumentParser(description="Crée un compte utilisateur.")
    parser.add_argument("identifiant")
    parser.add_argument("role", type=Role, choices=list(Role))
    args = parser.parse_args()

    init_db()
    with SessionLocal() as session:
        if session.scalar(select(Utilisateur).where(Utilisateur.identifiant == args.identifiant)):
            parser.error(f"le compte {args.identifiant} existe déjà")
        utilisateur = Utilisateur(identifiant=args.identifiant, role=args.role)
        utilisateur.definir_mot_de_passe(getpass.getpass("Mot de passe : "))
        session.add(utilisateur)
        session.commit()
    print(f"Compte {args.identifiant} créé.")


if __name__ == "__main__":
    main()
