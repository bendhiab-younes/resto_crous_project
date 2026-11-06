# Backlog produit

Le backlog vivant est tenu sur **Notion** et partagé avec l'enseignant (PO). Le sujet de TP
demande de *« donner accès à ces outils à l'enseignant **ou** de réaliser des exports dans un
format ouvert »* : on fait les deux.

Les fichiers de ce dossier sont des **exports CSV** (format ouvert, lisible et diffable) :

| Fichier | Contenu |
| --- | --- |
| [`epics.csv`](epics.csv) | Les 8 epics : grands thèmes métier, priorité MoSCoW |
| [`stories.csv`](stories.csv) | Les 22 user stories : epic, formulation, priorité, points, sprint |
| [`sprints.csv`](sprints.csv) | Les 6 sprints : objectif, points planifiés, capacité, vélocité |
| [`tasks.csv`](tasks.csv) | Les tâches : type, story, sprint, assigné, heures estimées et réelles, statut |

## Règle de mise à jour

- **Source de vérité : Notion.** On ne modifie pas les CSV à la main, sinon les deux versions
  divergent et aucune des deux n'est fiable.
- **À la clôture de chaque sprint** : réexporter les 4 fichiers depuis Notion et les commiter
  (`docs(backlog): export du backlog fin de sprint N`). L'historique git donne alors
  l'évolution du backlog sprint par sprint — une trace précieuse pour le rapport et la
  rétrospective finale.

## Légende

- **Priorité (MoSCoW)** — `Must` : indispensable · `Should` : important · `Could` : si le temps
  le permet.
- **Points** — effort relatif estimé par l'équipe (1, 2, 3, 5), pas des heures.
- **Type de tâche** — `Dev` · `Test` · `Doc` (documentation, UML, rapport) · `Setup` (mise en
  place technique) · `Process` (gestion de projet).
