# Workflow de l'équipe

Ce document fixe les règles de travail décidées en sprint 0 (tâche **T-01**). Elles sont
volontairement simples : elles doivent être tenues par 4 personnes sur 5 séances de TP.

## 1. Règles git

- La branche `main` est **protégée** : pas de push direct, tout passe par une *pull request*.
- **Une branche par story ou par tâche**, créée depuis `dev` à jour, avec une PR vers `main`.
  Younes remet `dev` au niveau de `main` après chaque merge.
- Une PR doit être **relue et approuvée par Younes Ben Dhiab** avant le merge (`.github/CODEOWNERS`).
  Scrum Master et propriétaire du dépôt, il est le seul à pouvoir merger ses propres PR sans relecture.
- **Seul Younes merge dans `main`**, même après son approbation. Un ruleset GitHub (« Seul Younes
  merge dans main ») bloque toute mise à jour de `main` par quelqu'un d'autre qu'un admin du dépôt.
- Merge en **squash** pour garder un historique lisible, puis suppression de la branche.
- On ne commite jamais : fichiers générés, base de données locale, secrets (`.env`).

### Nommage des branches

```
<type>/<ID>-<description-courte-en-kebab-case>
```

| Type | Usage | Exemple |
| --- | --- | --- |
| `feature` | développement d'une user story | `feature/S-03-creation-recette` |
| `fix` | correction de bug | `fix/S-08-validation-stock-vide` |
| `test` | ajout de tests | `test/S-02-api-ingredients` |
| `docs` | documentation, UML, rapport | `docs/T-06-diagramme-classes` |
| `chore` | outillage, configuration | `chore/T-01-mise-en-place-ci` |

### Messages de commit

Format : `<type>(<ID>): <description à l'impératif>`

```
feat(S-03): ajoute le modèle Recette et ses lignes d'ingrédients
test(S-02): couvre les cas d'erreur du CRUD ingrédients
docs(T-05): ajoute le diagramme de cas d'usage
```

## 2. Traçabilité

C'est le point le plus important pour l'évaluation : on doit pouvoir **suivre un besoin du PO
jusqu'au code et au test** qui le satisfont.

```
Epic (E1) → Story (S-03) → Tâches (T-13, T-14, T-15) → branche → commits → PR → rapport de tests
```

En pratique, l'identifiant de la story ou de la tâche apparaît :

1. dans le **nom de la branche** ;
2. dans chaque **message de commit** ;
3. dans le **titre de la PR** et dans son corps (`Story : S-03`) ;
4. dans les lignes du **rapport de tests** (`docs/tests/`) ;
5. dans la **page de sprint** (`docs/sprints/`) qui liste les stories engagées et livrées.

## 3. Cycle d'une story

1. La story est priorisée avec le PO et estimée en points par l'équipe (sprint planning).
2. Elle est découpée en tâches, chaque tâche a **un responsable** et une **estimation en heures**.
3. Développement sur la branche dédiée, commits petits et fréquents.
4. Ouverture de la PR, relecture et approbation par Younes, corrections éventuelles.
5. Merge, mise à jour du board, report des **heures réelles** en face de l'estimation.
6. La story n'est « terminée » que si elle satisfait la
   [Definition of Done](docs/definition-of-done.md).

## 4. Revue de code — ce qu'on regarde

- Le comportement correspond-il à la story et à ses critères d'acceptation ?
- Les tests couvrent-ils le cas nominal **et** au moins un cas d'erreur ?
- Le code est-il lisible (noms explicites, pas de duplication évidente) ?
- La documentation impactée est-elle mise à jour ?

Une remarque de revue n'est pas un reproche : on commente le code, pas la personne.

## 5. Rituels Scrum (une séance de TP = un sprint)

| Rituel | Quand | Durée | Trace produite |
| --- | --- | --- | --- |
| Démo au PO | début de séance | ~15 min | CR de réunion |
| Sprint planning | après la démo | ~20 min | page de sprint + board à jour |
| Point d'avancement | milieu de séance | ~5 min | — |
| Revue de sprint + rétrospective | fin de séance | ~15 min | page de sprint (bilan, actions) |

Toute décision prise avec le PO est consignée dans `docs/reunions/` **le jour même**.
