# ADR 0001 — Choix de la stack technique

- **Statut** : proposé (décision à acter en équipe, tâche **T-02**)
- **Date** : 2026-10-13
- **Participants** : toute l'équipe
- **Décideurs** : l'équipe de développement (le PO ne se prononce pas sur la technique)

## Contexte

Le projet est un gestionnaire de menus et de recettes à construire **de zéro** (pas de wrapper
autour d'un outil existant), sur **5 séances de TP**. Les contraintes qui pèsent sur le choix :

1. **Temps de mise en route très court** : un sprint = une séance, il faut livrer une
   fonctionnalité démontrable dès le sprint 1.
2. **Compétences hétérogènes** dans l'équipe de 4 personnes : la stack doit être connue ou
   apprenable en une séance.
3. **Besoins fonctionnels identifiés** : persistance relationnelle (ingrédients, recettes,
   menus, stock), calculs dérivés (nutrition, coût, allergènes), **export PDF**, **API REST**
   pour un site externe, authentification et rôles.
4. **Tests automatisés obligatoires** (rapports de tests attendus dans les rendus) : il faut un
   framework de test simple et rapide à exécuter.
5. L'évaluation récompense **la conduite du projet plus que la technique** : la stack doit
   minimiser le temps passé sur l'outillage.

## Options envisagées

### Option A — Python 3.12 + FastAPI + SQLAlchemy + SQLite

- **+** Mise en route en quelques minutes, très peu de configuration.
- **+** API REST et documentation OpenAPI générée automatiquement (couvre la story S-22).
- **+** `pytest` : tests lisibles, exécution quasi instantanée.
- **+** SQLite = un fichier, aucun serveur à installer sur 4 machines différentes.
- **+** PDF faisable simplement (`reportlab` / `weasyprint`) pour S-16 et S-17.
- **−** Front à faire avec des templates (Jinja2) : rendu visuel moins riche qu'un SPA.
- **−** Typage dynamique : erreurs détectées plus tard (atténué par Pydantic).

### Option B — Java 21 + Spring Boot + JPA + H2

- **+** Écosystème très structuré, typage statique, JUnit bien outillé.
- **+** Proche de ce qui est vu ailleurs dans le cursus.
- **−** Verbosité et temps de mise en route (Maven/Gradle, configuration) coûteux sur 5 séances.
- **−** Cycle de compilation plus lent, friction plus forte pour une équipe hétérogène.

### Option C — TypeScript : Node/Express + React + SQLite

- **+** Un seul langage du front au back, front le plus riche.
- **+** Typage statique, écosystème très fourni.
- **−** **Deux codebases** à construire, tester et démontrer : charge doublée pour 4 personnes.
- **−** Outillage (bundler, lint, config de test) consomme une part importante du sprint 1.

### Option D — Application de bureau (Python + Tkinter / Java + JavaFX)

- **+** Pas de couche HTTP à gérer.
- **−** L'API REST demandée (E7 / S-22) devient artificielle.
- **−** Démo moins pratique et tests d'interface plus coûteux.

## Critères de comparaison

| Critère | A (FastAPI) | B (Spring) | C (Node+React) | D (Desktop) |
| --- | --- | --- | --- | --- |
| Temps de mise en route | ++ | − | − | + |
| Compétences dans l'équipe | *à évaluer* | *à évaluer* | *à évaluer* | *à évaluer* |
| Facilité des tests | ++ | + | + | − |
| API REST (S-22) | ++ | + | + | −− |
| Export PDF (S-16, S-17) | + | + | + | + |
| Charge totale sur 5 sprints | ++ | − | −− | + |

## Décision

<!--
À REMPLIR EN ÉQUIPE (T-02). Formuler ainsi :
« Nous retenons l'option X parce que … Nous écartons Y parce que … »
Ne pas pré-remplir : la décision collective fait partie de la production évaluée.
-->

_Option retenue : …_

## Conséquences

À compléter après la décision. Pistes à documenter :

- outils à installer par chaque membre et comment on vérifie que ça tourne ;
- structure de dossiers du projet et convention de nommage ;
- commandes de référence (lancer l'application, lancer les tests) à mettre dans le README ;
- ce que la décision nous ferme (par exemple : pas de front SPA dans le périmètre) ;
- point de réexamen : si à la fin du sprint 1 la stack coûte plus qu'elle ne rapporte, on
  rouvre cet ADR plutôt que de subir le choix.
