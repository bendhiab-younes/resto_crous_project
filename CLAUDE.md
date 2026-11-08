# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## État du dépôt

Projet de TP (Processus du développement logiciel) conduit en Scrum : une séance de TP = un
sprint, l'enseignant est le client / Product Owner. Le produit est un gestionnaire de menus et de
recettes pour un restaurant universitaire.

Le squelette de l'application est en place (T-22), mais aucune story n'est encore livrée. L'évaluation récompense la conduite du projet plus que la technique (voir
`docs/rapport/plan-du-rapport.md`) : la documentation de suivi est un livrable noté, au même titre
que le code.

La stack **Python 3.12 · FastAPI · SQLAlchemy · SQLite · pytest**, avec un front en templates Jinja2
(pas de SPA), a été retenue par l'équipe le 06/11/2026 (`docs/adr/0001-choix-de-la-stack.md`).

## Commandes

```bash
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload     # http://127.0.0.1:8000
pytest                            # toute la suite
pytest -v                         # commande de référence des rapports de tests
pytest -k TC_S02                  # les tests d'une story
pytest -k TC_S02_03               # un seul cas de test
```

Aucun linter ni formateur n'est configuré.

## Structure du code

- `app/main.py` crée l'application et monte les routers, `app/database.py` fournit `Base`, `get_db`
  et `init_db`.
- **Nouveau modèle** : l'importer dans `app/models/__init__.py`, sinon sa table n'est pas créée.
  Les tables sont créées au démarrage par `init_db`, sans outil de migration : après un changement
  de modèle, supprimer `resto.db` en local.
- **Nouvelles routes** : un fichier par thème dans `app/routers/`, à monter dans `app/main.py`.
- **Pages** : les templates dans `app/templates/` étendent `base.html`, utiliser `templates` de
  `app/templating.py`.
- **Tests** : les fixtures `client` et `db` de `tests/conftest.py` utilisent une base en mémoire
  neuve à chaque test.

## Ce qui ne doit pas être inventé

Plusieurs contenus doivent venir de l'équipe : les rédiger à sa place fausse un livrable évalué.

- **Section « Décision » des ADR** : ne pas la pré-remplir, la décision collective fait partie de
  la production évaluée.
- **Données de suivi** : heures réelles, capacité, vélocité, dates, résultats de tests, décisions
  du PO, comptes rendus et rétrospectives. Les documents de suivi sont remplis pendant la séance,
  jamais reconstitués après coup. Laisser les marqueurs `<JJ/MM/AAAA>`, `<nom>`, `*à renseigner*`
  tant que l'équipe n'a pas fourni l'information.
- **`docs/backlog/*.csv`** : ne pas les modifier à la main. Ce sont des exports du board GitHub
  Projects, qui est la source de vérité ; ils sont mis à jour à la clôture de chaque sprint.
- **Besoins fonctionnels** : ils appartiennent au PO. En cas de doute, poser la question à
  l'équipe plutôt que de supposer ; la réponse va dans un CR de `docs/reunions/`.

## Conventions

`CONTRIBUTING.md` fait référence pour le workflow, `docs/definition-of-done.md` pour les critères
de « terminé ». L'essentiel :

- **Traçabilité** (point le plus important pour l'évaluation) : un besoin doit se suivre de l'epic
  jusqu'au test. L'identifiant `S-xx` ou `T-xx` apparaît dans la branche, chaque commit, le titre
  et le corps de la PR, le rapport de tests et la page de sprint.
- **Git** : `main` est protégée, tout passe par une PR approuvée par Younes. Lui seul merge dans
  `main` (ruleset GitHub), y compris ses propres PR sans relecture. Une branche par story ou tâche.
- **Branche** : `<type>/<ID>-<description-en-kebab-case>` avec `feature`, `fix`, `test`, `docs` ou
  `chore`, par exemple `feature/S-03-creation-recette`.
- **Commit** : `<type>(<ID>): <description à l'impératif>` en français, par exemple
  `feat(S-03): ajoute le modèle Recette et ses lignes d'ingrédients`.
- **Tests** : toute story livrée a au moins un test du cas nominal et un test d'un cas d'erreur.
  Cas de test `TC-<ID story>-<numéro>`, repris dans le nom de la fonction :
  `def test_TC_S02_03_cout_negatif_refuse():`. Les résultats vont dans `docs/tests/sprint-N.md`.
  Les calculs métier sont prioritaires (`docs/tests/README.md`).
- **Documents** : en français, nommés en kebab-case, référencés depuis `docs/README.md`.
- **Templates** : ne jamais modifier un `TEMPLATE-*.md`, le copier (`sprint-N.md`, `CR-…md`, etc.).
- **UML** : diagrammes Mermaid dans `docs/uml/`, mis à jour dans la même PR que le code qui change
  le modèle.
- **Décisions techniques** : toute décision donne lieu à un ADR dans `docs/adr/`.

## Modèle métier

Sources : `docs/uml/classes.md` (avec la justification des choix de modélisation),
`docs/uml/sequence-validation.md`, `docs/backlog/stories.csv`. Les critères d'acceptation du sprint
en cours sont dans `docs/sprints/sprint-N.md`. Les noms du domaine sont en français.

- **`Ingredient`** est à la racine : il porte le coût, la nutrition (pour 100 g) et les allergènes
  dont dépendent tous les calculs. Chemin critique : S-02 → S-03 → S-04 → S-08, puis S-09/S-11 →
  S-16.
- **`Recette`** : nutrition, coût et allergènes sont **dérivés** de ses `LigneRecette` (qui portent
  la quantité), jamais saisis. Les allergènes sont l'union de ceux des ingrédients.
  `ValeurNutritionnelle` est un *value object*, pas une entité.
- **Workflow de validation** : `statut` est un état de la recette,
  `BROUILLON` → `A_VALIDER` → `VALIDEE` ou `REFUSEE`. Le chef propose, l'intendant décide selon le
  stock et donne un motif en cas de refus.
- **`Stock`** est simulé et séparé d'`Ingredient`, pour pouvoir être remplacé par un vrai système.
- **`Menu`** : un jour d'un cycle de 2 semaines, 5 `LigneMenu` exactement (2 protéines, 1 féculent,
  1 légume, 1 végétarien), uniquement à partir de recettes `VALIDEE`.
- **Rôles** : `CHEF`, `INTENDANT`, `GESTION_CENTRALE`. L'usager consulte sans compte.
- **Périmètre** : l'API pour site externe (S-22) et l'alerte de cycle (S-21) sont des stories
  `Could` hors sprint, variables d'ajustement du planning.

## Organisation de la documentation

`docs/README.md` indexe tout et fait correspondre les rendus attendus aux fichiers. Le dépôt est la
référence unique pour les rendus. `docs/rapport/plan-du-rapport.md` indique la source de chaque
section du rapport final. `notes/` est ignoré par git et personnel.
