# Suivi des sprints

Une séance de TP = un sprint. Chaque sprint a sa page : objectif, stories engagées, tâches avec
estimation et heures réelles, démo, tests, bilan chiffré et rétrospective.

| Sprint | Page | Objectif | Pts planifiés | Capacité (h) | Vélocité |
| --- | --- | --- | --- | --- | --- |
| 0 | [sprint-0.md](sprint-0.md) | Cadrage : dépôt, stack, outils de suivi, règles d'équipe | 0 | *à renseigner* | — |
| 1 | [sprint-1.md](sprint-1.md) | Connexion, ingrédients et recettes | 15 | *à renseigner* | *à renseigner* |
| 2 | *à créer* | Calculs, rôles, validation, stock | 19 | | |
| 3 | *à créer* | Menus, cycle, coût, allergènes, alerte de stock | 20 | | |
| 4 | *à créer* | PDF, notifications, nutrition de menu | 14 | | |
| 5 | *à créer* | Stabilisation, démo et présentation finale, rapport | 0 | | |

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
