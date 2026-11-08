# Suivi des sprints

Une séance de TP = un sprint. Chaque sprint a sa page : objectif, stories engagées, tâches avec
estimation et heures réelles, démo, tests, bilan chiffré et rétrospective.

| Sprint | Séance | Page | Objectif | Pts planifiés | Capacité (h) | Vélocité |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 17/09 → 06/11 | [sprint-0.md](sprint-0.md) | Cadrage : dépôt, stack, outils de suivi, règles d'équipe | 0 | non renseignée | — |
| 1 | 06/11 | [sprint-1.md](sprint-1.md) | Connexion et ingrédients (S-01, S-02) | 10 | 12 + hors séance | *à renseigner* |
| 2 | 09/11 | *à créer* | Recettes, calculs, stock (S-03, S-04, S-07) | 13 | 12 + hors séance | |
| 3 | 10/12 | *à créer* | Validation et menus (S-06, S-08, S-09, S-10, S-12) | 16 | 12 + hors séance | |
| 4 | 17/12 | *à créer* | Clôture : démo finale, présentation, rapport | 0 | 12 | |

Les stories « à placer » (29 points) entrent dans un sprint dès que la vélocité le permet. Détail
du calendrier : [`../planning-gantt.md`](../planning-gantt.md).

Nouveau sprint : copier [`TEMPLATE-sprint.md`](TEMPLATE-sprint.md) en `sprint-N.md` et le remplir
**pendant** la séance, pas après.

## Capacité : comment la calculer

```
capacité (h) = nb de membres présents × (durée de la séance + heures prévues hors séance)
```

Exemple pour une séance de 3 h et 4 membres sans travail hors séance : 4 × 3 = **12 h**.
Sans cette valeur, on ne peut pas comparer la charge planifiée à ce que l'équipe peut absorber —
c'est elle qui justifie d'engager plus ou moins de stories au sprint suivant.

## Vélocité

Vélocité = somme des points des stories **terminées au sens de la
[Definition of Done](../definition-of-done.md)** à la clôture du sprint. Une story à 90 % compte
pour 0 point. La vélocité des sprints passés sert de base à l'engagement du sprint suivant.
