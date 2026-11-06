# Definition of Done (T-03)

Une story n'est pas « finie quand le code marche sur mon poste » : elle est finie quand les
critères ci-dessous sont **tous** vrais. Cette définition a été arrêtée en sprint 0 et s'applique
à toutes les stories du backlog.

## Pour une user story

| # | Critère | Comment on le vérifie |
| --- | --- | --- |
| 1 | Les critères d'acceptation de la story sont satisfaits | Démo manuelle par l'auteur, puis par le relecteur |
| 2 | Le code est sur `main` via une PR relue et approuvée | Historique git, PR fermée |
| 3 | Au moins un test automatisé couvre le cas nominal | `pytest` |
| 4 | Au moins un cas d'erreur ou limite est testé | `pytest` |
| 5 | Toute la suite de tests passe | `pytest` en local avant le merge |
| 6 | Le résultat des tests est consigné | Ligne ajoutée dans `docs/tests/sprint-N.md` |
| 7 | La documentation impactée est à jour | README, UML, ADR si une décision a été prise |
| 8 | Les heures réelles sont reportées en face de l'estimation | Board (colonne « Réel (h) ») |
| 9 | La story est démontrable au PO en fin de séance | Scénario de démo rejoué une fois |

## Pour une tâche de documentation ou de projet

| # | Critère |
| --- | --- |
| 1 | Le livrable est commité dans le dépôt (ou exporté dans un format ouvert) |
| 2 | Il est relu par un autre membre de l'équipe |
| 3 | Il est référencé depuis l'index `docs/README.md` |
| 4 | Les heures réelles sont reportées sur le board |

## Definition of Ready (avant d'engager une story dans un sprint)

Une story n'entre dans un sprint que si :

- elle est formulée « En tant que … je veux … afin de … » ;
- elle a des **critères d'acceptation** explicites ;
- elle est **estimée** en points par l'équipe ;
- elle est découpée en tâches avec un responsable et une estimation en heures ;
- elle ne dépend pas d'une autre story non livrée (ou la dépendance est planifiée avant).

## Ce qu'on s'interdit

- Merger sa propre PR sans relecture.
- Déclarer une story « faite » sans test automatisé.
- Reporter la mise à jour du board ou du CR de réunion « à plus tard » : on le fait en séance.
- Laisser du code mort ou commenté « au cas où » : git garde l'historique.
