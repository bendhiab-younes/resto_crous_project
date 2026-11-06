# Gestionnaire de menus et de recettes

Projet de TP — **Processus du développement logiciel** (2026-2027, semestre 1).
Conduite du projet en **Scrum**, une séance de TP = un sprint, l'enseignant joue le rôle de
client / Product Owner.

## Le produit

Plateforme de gestion des menus d'un restaurant universitaire :

- gestion des **ingrédients** (allergènes, valeurs nutritionnelles, coût) ;
- création de **recettes** (ingrédients + quantités, procédure) avec calcul automatique de la
  nutrition, des allergènes et du coût ;
- **workflow de validation** : le chef propose une recette, l'intendant la valide ou la refuse
  selon la disponibilité des ingrédients (stock simulé) ;
- composition de **menus** sur un cycle de 2 semaines, uniquement à partir de recettes validées ;
- **information des usagers** : menu du jour, allergènes, nutrition ;
- **export PDF** des menus et des recettes, **API** pour un site externe.

## Équipe et rôles

| Membre | Rôle |
| --- | --- |
| Adam Youssef--Muzzi | Développement, documentation et modélisation UML |
| Younes Ben Dhiab | **Scrum Master** + développement, process et qualité |
| Aziz Mdallel | Développement, outils de suivi et backlog |
| Youssef Essid | Développement, stratégie et rapports de tests |
| Enseignant | Client / Product Owner |

Détail et responsabilités : [`docs/roles.md`](docs/roles.md).

## Stack technique

**Python 3.12 · FastAPI · SQLAlchemy · SQLite · pytest**
Décision et comparatif des options : [`docs/adr/0001-choix-de-la-stack.md`](docs/adr/0001-choix-de-la-stack.md).

## Mise en route

```bash
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload     # http://127.0.0.1:8000
pytest                            # lance la suite de tests
```

## Documentation du projet

| Document | Contenu |
| --- | --- |
| [`docs/`](docs/) | Index de toute la documentation |
| [`docs/backlog/`](docs/backlog/) | Epics, user stories, sprints, tâches (export format ouvert) |
| [`docs/sprints/`](docs/sprints/) | Une page par sprint : objectif, engagement, vélocité, rétrospective |
| [`docs/reunions/`](docs/reunions/) | Comptes rendus des réunions avec le PO |
| [`docs/uml/`](docs/uml/) | Diagrammes de cas d'usage et de classes |
| [`docs/planning-gantt.md`](docs/planning-gantt.md) | Planning prévisionnel (Gantt) |
| [`docs/tests/`](docs/tests/) | Rapports de tests par sprint |
| [`docs/definition-of-done.md`](docs/definition-of-done.md) | Critères de « terminé » |
| [`docs/adr/`](docs/adr/) | Décisions d'architecture (ADR) |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Workflow git, conventions de nommage, revue de code |

Le suivi vivant (board, estimations) est tenu sur GitHub Projects et partagé avec l'enseignant ;
un export au format ouvert est commité dans [`docs/backlog/`](docs/backlog/) à la clôture de
chaque sprint.
