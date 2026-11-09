# Rapports de tests

Le sujet attend des **rapports de tests** dans les rendus. On produit un rapport **par sprint**,
rédigé au fil de l'eau (pas reconstitué à la fin), à partir du template
[`TEMPLATE-rapport-de-tests.md`](TEMPLATE-rapport-de-tests.md).

| Sprint | Rapport |
| --- | --- |
| 1 | *à créer : `sprint-1.md`* |
| 2 | [`sprint-2.md`](sprint-2.md) |
| 3 | *à créer* |
| 4 | *à créer* |
| 5 | *consolidation pour le rapport final (T-18)* |

## Stratégie de test

| Niveau | Ce qu'on teste | Outil |
| --- | --- | --- |
| **Unitaire** | Les calculs : coût d'une recette, nutrition pour 100 g, union des allergènes, suffisance du stock | `pytest` |
| **Intégration (API)** | Les endpoints : codes de retour, validation des entrées, droits selon le rôle | `pytest` + client de test HTTP |
| **Manuel / acceptation** | Les parcours démontrés au PO, à partir des critères d'acceptation de la story | checklist dans le rapport de sprint |

Règle issue de la [Definition of Done](../definition-of-done.md) : **toute story livrée a au moins
un test du cas nominal et un test d'un cas d'erreur.** Les calculs métier sont prioritaires pour
les tests automatisés — ce sont eux qui portent le risque de faux résultats silencieux.

## Convention de nommage des cas de test

```
TC-<ID story>-<numéro>   ex. TC-S02-03
```

L'identifiant apparaît dans le nom de la fonction de test, pour relier le code au rapport :

```python
def test_TC_S02_03_cout_negatif_refuse():
    ...
```
