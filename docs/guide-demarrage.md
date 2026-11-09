# Guide de démarrage

Tout ce qu'il faut pour lancer le projet et livrer une tâche. Les règles complètes sont dans
[`CONTRIBUTING.md`](../CONTRIBUTING.md).

## 1. Installer et lancer le projet

Il faut Python 3.12 (`python3.12 --version`) et git.

```bash
git clone https://github.com/bendhiab-younes/resto_crous_project.git
cd resto_crous_project
git switch dev
python3.12 -m venv .venv
source .venv/bin/activate            # Windows : .venv\Scripts\activate
pip install -r requirements.txt
pytest                               # tout doit passer
```

Créer un compte local, puis lancer l'application :

```bash
python -m app.creer_utilisateur moi CHEF    # demande un mot de passe
uvicorn app.main:app --reload
```

Pour changer de rôle : `python -m app.changer_role moi INTENDANT`.

Ouvrir <http://127.0.0.1:8000> et se connecter. Le compte existe seulement dans `resto.db`, sur
votre machine. Si un modèle change, supprimer `resto.db` et recréer le compte.

## 2. Qui fait quoi

| Membre | Tâches |
| --- | --- |
| Adam | [T-05](https://github.com/bendhiab-younes/resto_crous_project/issues/28), [T-06](https://github.com/bendhiab-younes/resto_crous_project/issues/29), [T-09](https://github.com/bendhiab-younes/resto_crous_project/issues/32), [T-12](https://github.com/bendhiab-younes/resto_crous_project/issues/35), [T-15](https://github.com/bendhiab-younes/resto_crous_project/issues/38) |
| Youssef | [T-23](https://github.com/bendhiab-younes/resto_crous_project/issues/50) |
| Aziz | [T-24](https://github.com/bendhiab-younes/resto_crous_project/issues/51) |

Chaque issue donne le contrat à respecter : noms de champs, variables de template, signatures et
tests attendus. Le suivi est sur le [board](https://github.com/users/bendhiab-younes/projects/1) :
passer sa tâche à « En cours » en commençant, puis renseigner les heures réelles à la fin.

## 3. Livrer une tâche

```bash
git switch dev && git pull
git switch -c feature/T-12-pages-ingredients    # le nom de branche indiqué dans l'issue
# coder, puis :
pytest
git add <fichiers>
git commit -m "feat(T-12): ajoute la liste des ingrédients"
git push -u origin feature/T-12-pages-ingredients
```

Ouvrir ensuite une pull request **vers `main`** et remplir le modèle proposé. Seul Younes approuve
et merge. Après chaque merge, il remet `dev` au niveau de `main` : refaire `git switch dev && git pull`
avant de commencer la tâche suivante.

Les commits suivent le format `<type>(<ID>): <description à l'impératif>`, en français. Une tâche =
une branche. Ne jamais commiter `resto.db`, `.venv/` ni de secret.

## 4. Où travailler dans le code

| Besoin | Fichier |
| --- | --- |
| Pages | `app/templates/` (étendent `base.html`) |
| Style | `app/static/style.css` |
| Routes | `app/routers/` |
| Modèles | `app/models/` |
| Tests | `tests/`, fixtures `client`, `client_connecte` et `db` dans `conftest.py` |

Les pages actuelles sont provisoires : T-09, T-12 et T-15 les remplacent, sans changer les noms de
variables ni de champs. Les tests de `tests/test_connexion.py`, `test_ingredients.py` et
`test_recettes.py` doivent rester verts.

**Charte graphique** : couleurs et police des Crous, dans les variables en tête de `style.css`
(`--rouge`, `--encre`, etc.). Réutiliser ces variables et les classes `bouton` et `erreur`, sans
ajouter de nouvelles couleurs.

## 5. Outils d'IA

Claude Code, GitHub Copilot et les outils du même type sont autorisés par le PO. Relire et
comprendre ce qui est généré avant de l'ouvrir en PR : chacun reste responsable de son code et doit
pouvoir l'expliquer.
