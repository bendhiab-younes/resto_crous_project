# GitHub Project

## Configuration

Le suivi vivant du projet est réalisé dans un **[GitHub Project](https://github.com/users/bendhiab-younes/projects/1)** rattaché au compte
`bendhiab-younes` et au dépôt `resto_crous_project`.

| Paramètre | Valeur |
| --- | --- |
| Nom | Resto CROUS — Gestionnaire de menus |
| Propriétaire | `bendhiab-younes` |
| Visibilité | Public |
| Vue principale | Board (colonnes À faire, En cours, En revue, Terminé) |
| Vue complémentaire | Table |
| Import initial | Stories `S-01` à `S-22` et tâches `T-01` à `T-22` |

## Champs de suivi

Le Project permet de suivre :

- le statut de l'élément ;
- le sprint (`Sprint 0` à `Sprint 4`, `À placer` ou `Backlog`) ;
- la priorité MoSCoW (`Must`, `Should`, `Could`) ;
- les points des stories, les heures estimées et réelles des tâches ;
- le type (`Story`, `Dev`, `Test`, `Doc`, `Setup`, `Process`) ;
- l'epic associée, par un label ;
- le lien avec l'issue, la branche et la pull request.

Les valeurs initiales proviennent des exports présents dans [`docs/backlog/`](backlog/).
Le board GitHub Projects est la source de vérité. Les exports CSV sont actualisés à la clôture de chaque sprint.

## Règles d'utilisation

1. Une issue est créée pour chaque story et chaque tâche.
2. L'identifiant apparaît dans le titre de l'issue : `S-03 — ...` ou `T-13 — ...`.
3. Les issues sont affectées au sprint et à la priorité correspondants.
4. Les branches, commits et pull requests reprennent l'identifiant de la story ou de la tâche.
5. Les heures réelles et le statut sont renseignés pendant le sprint.
6. À la clôture du sprint, les CSV sont mis à jour à partir du board puis commités.
7. Le Project est partagé avec l'enseignant, qui joue le rôle de Product Owner.
