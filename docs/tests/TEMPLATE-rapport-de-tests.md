# Rapport de tests — Sprint <N> — <JJ/MM/AAAA>

- **Périmètre testé** : stories S-0X, S-0Y
- **Responsable des tests** : <nom>
- **Environnement** : Python <version>, SQLite, `pytest <version>`, macOS / Linux
- **Commande** : `pytest -v`

## 1. Synthèse

| Indicateur | Valeur |
| --- | --- |
| Cas de test exécutés | |
| Réussis | |
| Échoués | |
| Non exécutés (bloqués) | |
| Couverture (si mesurée) | |

Verdict : *le périmètre du sprint est / n'est pas validé*, parce que …

## 2. Cas de test

| ID | Story | Niveau | Cas testé | Résultat attendu | Résultat obtenu | Statut |
| --- | --- | --- | --- | --- | --- | --- |
| TC-S0X-01 | S-0X | unitaire | | | | ✅ / ❌ |
| TC-S0X-02 | S-0X | API | | | | ✅ / ❌ |
| TC-S0X-03 | S-0X | API (cas d'erreur) | | | | ✅ / ❌ |
| TC-S0X-04 | S-0X | manuel | | | | ✅ / ❌ |

## 3. Anomalies relevées

| # | Cas de test | Description | Gravité | Décision | Statut |
| --- | --- | --- | --- | --- | --- |
| B-01 | TC-S0X-02 | | bloquante / majeure / mineure | corrigée dans le sprint / reportée / acceptée | |

*Gravité* — **bloquante** : empêche d'utiliser la fonctionnalité · **majeure** : résultat faux ou
contournement nécessaire · **mineure** : gêne sans conséquence fonctionnelle.

## 4. Tests manuels d'acceptation (démo PO)

| Étape du scénario | Attendu | Observé | OK |
| --- | --- | --- | --- |
| 1. | | | ☐ |
| 2. | | | ☐ |

## 5. Ce qui n'est pas testé (dette de test assumée)

| Zone non couverte | Pourquoi | Quand on la couvre |
| --- | --- | --- |
| | | |

## 6. Sortie brute de la suite de tests

```
<coller ici la sortie de `pytest -v`, ou le résumé des dernières lignes>
```
