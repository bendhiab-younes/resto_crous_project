# Rapport de tests — Sprint 2 — 09/11/2026

- **Périmètre testé** : stories S-02, S-03, S-04, S-05, S-06 (tâche T-16). S-07 et S-08, mergées pendant cette tâche, seront comparées à leurs critères dans la suite de T-16.
- **Responsable des tests** : Youssef Essid
- **Environnement** : Python 3.12.10, SQLite, `pytest 9.2.0`, Windows 11
- **Commande** : `pytest -v`

## 1. Synthèse

| Indicateur | Valeur |
| --- | --- |
| Cas de test exécutés | 100 (S-02 à S-06), dont 22 ajoutés par T-16 |
| Réussis | 100 |
| Échoués | 0 |
| Non exécutés (bloqués) | 0 |
| Couverture (si mesurée) | non mesurée |

Une fonction de test à plusieurs variantes compte pour une ligne dans le tableau, et pour autant de cas que de variantes dans ce total.

Verdict : *les tests automatisés de S-02 à S-06 sont tous réussis ; la validation du périmètre reste à prononcer après la démo au PO et le traitement des anomalies de la section 3.*

## 2. Cas de test

| ID | Story | Niveau | Cas testé | Résultat attendu | Résultat obtenu | Statut |
| --- | --- | --- | --- | --- | --- | --- |
| TC-S02-01 | S-02 | API | Créer un ingrédient complet | Redirection, tous les champs enregistrés | Conforme | ✅ |
| TC-S02-02 | S-02 | API (cas d'erreur) | Nom vide à la création | Refus 422, message, rien d'enregistré | Conforme | ✅ |
| TC-S02-03 | S-02 | API (cas d'erreur) | Coût négatif à la création | Refus 422, message, rien d'enregistré | Conforme | ✅ |
| TC-S02-04 | S-02 | API (cas d'erreur) | Nom déjà pris, sans tenir compte de la casse | Refus 422, message, pas de doublon | Conforme | ✅ |
| TC-S02-05 | S-02 | API (cas d'erreur) | Valeur non numérique | Refus 422, message dans la page HTML | Conforme | ✅ |
| TC-S02-06 | S-02 | API (cas d'erreur) | Valeurs `nan` et `inf` | Refus 422, rien d'enregistré | Conforme | ✅ |
| TC-S02-07 | S-02 | API | Virgule décimale | `2,5` enregistré comme 2.5 | Conforme | ✅ |
| TC-S02-08 | S-02 | API (cas d'erreur) | Allergène inconnu | Refus 422, rien d'enregistré | Conforme | ✅ |
| TC-S02-09 | S-02 | API (cas d'erreur) | Saisie après une erreur | La saisie reste dans le formulaire | Conforme | ✅ |
| TC-S02-10 | S-02 | API | Liste des ingrédients | Ingrédient et allergènes affichés | Conforme | ✅ |
| TC-S02-11 | S-02 | API | Formulaire de création | Allergènes proposés | Conforme | ✅ |
| TC-S02-12 | S-02 | API | Formulaire de modification | Valeurs préremplies | Conforme | ✅ |
| TC-S02-13 | S-02 | API | Modification | Nouvelles valeurs enregistrées | Conforme | ✅ |
| TC-S02-14 | S-02 | API | Modification sans changer le nom | Acceptée | Conforme | ✅ |
| TC-S02-15 | S-02 | API (cas d'erreur) | Modification vers un nom pris | Refus 422, nom inchangé | Conforme | ✅ |
| TC-S02-16 | S-02 | API | Suppression | Ingrédient supprimé | Conforme | ✅ |
| TC-S02-17 | S-02 | API (cas d'erreur) | Ingrédient inexistant | Réponse 404 | Conforme | ✅ |
| TC-S02-18 | S-02 | API (cas d'erreur) | Création sans session | Redirection, rien d'enregistré | Conforme | ✅ |
| TC-S02-19 | S-02 | unitaire | Chargement des allergènes réglementaires | Chargés une seule fois | Conforme | ✅ |
| TC-S02-20 | S-02 | API (cas d'erreur) | Coût négatif en modification *(ajout T-16)* | Refus 422, message, coût inchangé | Conforme | ✅ |
| TC-S02-21 | S-02 | API (cas d'erreur) | Nom vide en modification *(ajout T-16)* | Refus 422, message, nom inchangé | Conforme | ✅ |
| TC-S02-22 | S-02 | API (cas d'erreur) | Valeur nutritionnelle négative, pour chaque nutriment *(ajout T-16)* | Refus 422, message, rien d'enregistré | Conforme (4 variantes) | ✅ |
| TC-S02-23 | S-02 | API | Changement des allergènes d'un ingrédient *(ajout T-16)* | Nouveaux allergènes enregistrés | Conforme | ✅ |
| TC-S03-01 | S-03 | unitaire | Statut d'une nouvelle recette | `BROUILLON` | Conforme | ✅ |
| TC-S03-02 | S-03 | unitaire | Suppression d'une recette | Lignes supprimées, ingrédient conservé | Conforme | ✅ |
| TC-S03-03 | S-03 | unitaire | Suppression en base d'un ingrédient utilisé | Refusée par la contrainte | Conforme | ✅ |
| TC-S03-04 | S-03 | API | Créer une recette à plusieurs lignes | Champs, lignes, auteur et brouillon enregistrés | Conforme | ✅ |
| TC-S03-05 | S-03 | API | Case végétarien décochée | `vegetarien` faux | Conforme | ✅ |
| TC-S03-06 | S-03 | API | Lignes laissées vides | Ignorées | Conforme | ✅ |
| TC-S03-07 | S-03 | API (cas d'erreur) | Saisies invalides : titre, type, procédure, aucun ingrédient, quantité, ingrédient inconnu | Refus 422, message, rien d'enregistré | Conforme (9 variantes) | ✅ |
| TC-S03-08 | S-03 | API (cas d'erreur) | Saisie après une erreur | La saisie reste dans le formulaire | Conforme | ✅ |
| TC-S03-09 | S-03 | API | Liste des recettes | Recette affichée | Conforme | ✅ |
| TC-S03-10 | S-03 | API | Formulaire de création | Ingrédients proposés | Conforme | ✅ |
| TC-S03-11 | S-03 | API | Formulaire de modification | Valeurs préremplies | Conforme | ✅ |
| TC-S03-12 | S-03 | API | Modification | Titre changé, lignes remplacées | Conforme | ✅ |
| TC-S03-13 | S-03 | API (cas d'erreur) | Modification avec titre vide | Refus 422, titre inchangé | Conforme | ✅ |
| TC-S03-14 | S-03 | API | Suppression | Recette supprimée | Conforme | ✅ |
| TC-S03-15 | S-03 | API (cas d'erreur) | Recette inexistante | Réponse 404 | Conforme | ✅ |
| TC-S03-16 | S-03 | API (cas d'erreur) | Accès sans session | Redirection, rien d'enregistré | Conforme | ✅ |
| TC-S03-17 | S-03 | API (cas d'erreur) | Suppression d'un ingrédient utilisé | Refus 409, message, ingrédient conservé | Conforme | ✅ |
| TC-S03-18 | S-03 | API (cas d'erreur) | Modification sans ingrédient *(ajout T-16)* | Refus 422, message, lignes inchangées | Conforme | ✅ |
| TC-S03-19 | S-03 | API | Création avec chacun des 4 types de plat *(ajout T-16)* | Type enregistré | Conforme (4 variantes) | ✅ |
| TC-S04-01 | S-04 | unitaire | Coût d'une ligne | 2 € | Conforme | ✅ |
| TC-S04-02 | S-04 | unitaire | Coût de plusieurs lignes | 3 € | Conforme | ✅ |
| TC-S04-03 | S-04 | unitaire | Coût d'une liste vide | 0.0, de type float | Conforme | ✅ |
| TC-S04-04 | S-04 | unitaire | Nutrition d'une seule ligne | Valeurs de l'ingrédient | Conforme | ✅ |
| TC-S04-05 | S-04 | unitaire | Nutrition de plusieurs lignes | Moyenne pondérée : 140 / 9 / 21 / 1,5 | Conforme | ✅ |
| TC-S04-06 | S-04 | unitaire | Nutrition d'une liste vide | `ValueError` | Conforme | ✅ |
| TC-S04-07 | S-04 | unitaire | Nutrition d'une quantité totale nulle | `ValueError` | Conforme | ✅ |
| TC-S04-08 | S-04 | unitaire | Union des allergènes | Triée, sans doublon | Conforme | ✅ |
| TC-S04-09 | S-04 | unitaire | Ingrédient sans allergène | Liste vide | Conforme | ✅ |
| TC-S04-10 | S-04 | unitaire | Allergènes d'une liste vide | Liste vide | Conforme | ✅ |
| TC-S04-11 | S-04 | API | Contenu de la fiche | Titre, ingrédients et procédure affichés | Conforme | ✅ |
| TC-S04-12 | S-04 | API | Coût sur la fiche | 0,70 € | Conforme | ✅ |
| TC-S04-13 | S-04 | API | Nutrition sur la fiche | 150,0 / 7,0 / 31,0 / 1,9 | Conforme | ✅ |
| TC-S04-14 | S-04 | API | Allergènes sur la fiche | Gluten, Lait | Conforme | ✅ |
| TC-S04-15 | S-04 | API | Fiche sans allergène | « Aucun » | Conforme | ✅ |
| TC-S04-16 | S-04 | API (cas d'erreur) | Fiche inexistante | Réponse 404 | Conforme | ✅ |
| TC-S04-17 | S-04 | API (cas d'erreur) | Fiche sans session | Redirection | Conforme | ✅ |
| TC-S04-18 | S-04 | API | Lien depuis la liste | La liste mène à la fiche | Conforme | ✅ |
| TC-S04-19 | S-04 | API | Allergène commun à deux ingrédients *(ajout T-16)* | Affiché une seule fois | Conforme | ✅ |
| TC-S04-20 | S-04 | API | Fiche après modification d'un ingrédient *(ajout T-16)* | Recalculée : 1,10 € et 190,0 kcal | Conforme | ✅ |
| TC-S04-21 | S-04 | API | Fiche vue par l'intendant et la gestion centrale *(ajout T-16)* | Page affichée avec le coût | Conforme (2 variantes) | ✅ |
| TC-S05-01 | S-05 | unitaire | Rôle autorisé | Accès accordé | Conforme | ✅ |
| TC-S05-02 | S-05 | unitaire | Plusieurs rôles autorisés | Accès accordé | Conforme | ✅ |
| TC-S05-03 | S-05 | unitaire | Rôle non autorisé | Erreur 403 | Conforme | ✅ |
| TC-S05-04 | S-05 | unitaire | Changer le rôle d'un compte | Nouveau rôle enregistré | Conforme | ✅ |
| TC-S05-05 | S-05 | unitaire | Changer le rôle d'un compte inconnu | `ValueError`, aucun changement | Conforme | ✅ |
| TC-S05-06 | S-05 | API (cas d'erreur) | Rôle chef retiré pendant une session ouverte *(ajout T-16)* | Refus 403, statut inchangé | Conforme | ✅ |
| TC-S05-07 | S-05 | API | Rôle chef attribué pendant une session ouverte *(ajout T-16)* | Proposition acceptée | Conforme | ✅ |
| TC-S05-08 | S-05 | unitaire | Attribution de chacun des 3 rôles *(ajout T-16)* | Rôle enregistré | Conforme (3 variantes) | ✅ |
| TC-S06-01 | S-06 | API | Proposer un brouillon | Statut `A_VALIDER`, retour à la fiche | Conforme | ✅ |
| TC-S06-02 | S-06 | API (cas d'erreur) | Proposer une recette qui n'est pas en brouillon | Refus 409, message, statut inchangé | Conforme (3 variantes) | ✅ |
| TC-S06-03 | S-06 | API (cas d'erreur) | Proposition par l'intendant | Refus 403, page HTML, statut inchangé | Conforme | ✅ |
| TC-S06-04 | S-06 | API (cas d'erreur) | Proposition sans session | Redirection, statut inchangé | Conforme | ✅ |
| TC-S06-05 | S-06 | API (cas d'erreur) | Recette inexistante | Réponse 404 | Conforme | ✅ |
| TC-S06-06 | S-06 | API | Bouton pour le chef sur un brouillon | Visible | Conforme | ✅ |
| TC-S06-07 | S-06 | API | Bouton une fois proposée | Masqué | Conforme | ✅ |
| TC-S06-08 | S-06 | API | Bouton pour un autre rôle | Masqué | Conforme | ✅ |
| TC-S06-09 | S-06 | API | Statut sur la fiche | « À valider » | Conforme | ✅ |
| TC-S06-10 | S-06 | API (cas d'erreur) | Proposition par la gestion centrale *(ajout T-16)* | Refus 403, statut inchangé | Conforme | ✅ |

### Correspondance avec les critères d'acceptation

S-04, S-05 et S-06 n'ont pas de critères d'acceptation écrits dans leur issue. Elles sont comparées au texte de la story et aux contrats de T-23, T-25 et T-26.

| Story | Critère | Cas de test |
| --- | --- | --- |
| S-02 | Créer, lister, modifier et supprimer un ingrédient | 01, 10, 13, 16 |
| S-02 | Nom, allergènes, nutrition pour 100 g, coût | 01, 13, 23 |
| S-02 | Nom obligatoire et unique, coût négatif refusé | 02, 03, 04, 15, 20, 21 |
| S-02 | Erreurs de validation affichées | 02, 03, 05, 20, 21, 22 |
| S-03 | Titre, type, végétarien, procédure | 04, 05, 19 |
| S-03 | Plusieurs lignes ingrédient + quantité | 04, 12 |
| S-03 | Recette sans ingrédient refusée | 07, 18 |
| S-03 | Nouvelle recette en brouillon | 01, 04 |
| S-04 | Voir le coût | 01 à 03, 12, 20 |
| S-04 | Voir la nutrition pour 100 g | 04 à 07, 13, 20 |
| S-04 | Voir les allergènes | 08 à 10, 14, 15, 19 |
| S-04 | Fiche accessible aux utilisateurs connectés | 11, 16, 17, 18, 21 |
| S-05 | Accès autorisé ou refusé selon le rôle | 01, 02, 03, 06, 07 |
| S-05 | Attribution d'un rôle à un compte | 04, 05, 08 |
| S-06 | Un brouillon passe à « à valider » | 01, 09 |
| S-06 | Un autre statut ne permet pas de proposer | 02, 07 |
| S-06 | Seul le chef peut proposer | 03, 04, 06, 08, 10 |

## 3. Anomalies relevées

Comportements observés lors de T-16, sans échec de test : aucun critère écrit ne les tranche.

| # | Cas de test | Description | Gravité | Décision | Statut |
| --- | --- | --- | --- | --- | --- |
| B-01 | hors suite | Une recette `VALIDEE` peut être modifiée et reste `VALIDEE`, sans nouvelle validation | *à renseigner* | *à renseigner avec le PO* | ouverte |
| B-02 | hors suite | S-03 parle du chef, mais tout compte connecté, par exemple un intendant, peut créer, modifier et supprimer des recettes et des ingrédients | *à renseigner* | *à renseigner avec le PO* | ouverte |
| B-03 | hors suite | Le même ingrédient peut figurer sur plusieurs lignes d'une recette | *à renseigner* | *à renseigner avec le PO* | ouverte |
| B-04 | hors suite | La fiche d'une recette sans aucune ligne répond 500. Ce cas n'a été obtenu qu'en créant la recette directement en base, le formulaire exigeant un ingrédient | mineure | *à renseigner* | ouverte |

*Gravité* — **bloquante** : empêche d'utiliser la fonctionnalité · **majeure** : résultat faux ou
contournement nécessaire · **mineure** : gêne sans conséquence fonctionnelle.

## 4. Tests manuels d'acceptation (démo PO)

| Étape du scénario | Attendu | Observé | OK |
| --- | --- | --- | --- |
| *à renseigner pendant la démo* | | | ☐ |

## 5. Ce qui n'est pas testé (dette de test assumée)

| Zone non couverte | Pourquoi | Quand on la couvre |
| --- | --- | --- |
| Comparaison de S-07 et S-08 aux critères | Code mergé pendant cette tâche (T-28, T-27) ; leurs tests existants passent, mais les cas manquants n'ont pas été recherchés | Suite de T-16 |
| Modification et suppression d'un ingrédient sans session | Critère de S-01, hors du périmètre S-02 à S-06 | *à renseigner* |
| Rôle « administrateur » de S-05 | Absent des rôles du projet, à confirmer avec le PO (T-25) | Après la réponse du PO |
| Rendu visuel des pages | Les tests vérifient le contenu HTML, pas l'affichage | Démo au PO |

## 6. Sortie brute de la suite de tests

Résumé de `pytest -v` sur toute la suite, y compris les tests hors du périmètre S-02 à S-06 :

```
158 passed in 28.21s
```
