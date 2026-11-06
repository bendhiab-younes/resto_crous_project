# Sprint 1 — Connexion, ingrédients et recettes — <JJ/MM/AAAA>

- **Objectif du sprint** : un utilisateur peut se connecter, saisir des ingrédients et créer une
  recette. C'est la base de tout le reste du produit.
- **Scrum Master du sprint** : <nom>
- **Capacité** : <nb membres> × <heures> = **<X> h** *(à renseigner avant le planning)*
- **Engagement** : 15 points

## 1. Stories engagées

| Story | Intitulé | Pts | Responsable | Statut en fin de sprint |
| --- | --- | --- | --- | --- |
| S-01 | Authentification de l'utilisateur | 5 | | |
| S-02 | Gestion des ingrédients (allergènes, nutrition, coût) | 5 | | |
| S-03 | Création d'une recette (titre, type, végétarien, ingrédients, procédure) | 5 | | |

**Total engagé : 15 pts — Vélocité : <V> pts**

### Critères d'acceptation

**S-01 — Authentification**
- Un utilisateur enregistré peut se connecter avec identifiant + mot de passe.
- Le mot de passe est stocké **haché**, jamais en clair.
- Un mauvais mot de passe affiche un message d'erreur sans révéler si le compte existe.
- Les pages de l'application ne sont pas accessibles sans session valide.
- La déconnexion invalide la session.

**S-02 — Ingrédients**
- Créer, lister, modifier et supprimer un ingrédient.
- Un ingrédient porte : nom, allergènes, valeurs nutritionnelles (pour 100 g), coût unitaire.
- Le nom est obligatoire et unique ; un coût négatif est refusé.
- Les erreurs de validation sont affichées à l'utilisateur.

**S-03 — Recette**
- Créer une recette avec titre, type, caractère végétarien, procédure.
- Ajouter plusieurs lignes « ingrédient + quantité » à une recette.
- Une recette sans ingrédient est refusée.
- Une recette nouvellement créée est en statut « brouillon » (elle n'est pas encore proposée).

## 2. Tâches

| Tâche | Intitulé | Type | Story | Assigné | Est. (h) | Réel (h) | Statut |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T-05 | Diagramme de cas d'usage | Doc | — | Adam Youssef--Muzzi | 0.5 | | à faire |
| T-06 | Diagramme de classes | Doc | — | Adam Youssef--Muzzi | 1 | | à faire |
| T-07 | Modèle User + hash du mot de passe | Dev | S-01 | **à affecter** | 1 | | à faire |
| T-08 | Endpoints login/logout | Dev | S-01 | **à affecter** | 1 | | à faire |
| T-09 | Page de connexion | Dev | S-01 | **à affecter** | 0.5 | | à faire |
| T-10 | Modèle Ingrédient + migration | Dev | S-02 | **à affecter** | 0.5 | | à faire |
| T-11 | CRUD API ingrédients | Dev | S-02 | **à affecter** | 1 | | à faire |
| T-12 | Écrans liste et formulaire d'ingrédients | Dev | S-02 | Adam Youssef--Muzzi | 1.5 | | à faire |
| T-13 | Modèle Recette + lignes d'ingrédients | Dev | S-03 | **à affecter** | 1 | | à faire |
| T-14 | CRUD API recettes | Dev | S-03 | **à affecter** | 1 | | à faire |
| T-15 | Formulaire de recette | Dev | S-03 | Adam Youssef--Muzzi | 1.5 | | à faire |
| T-16 | Tests des API ingrédients et recettes | Test | S-02, S-03 | **à affecter** | 1 | | à faire |
| T-17 | Revue de sprint, CR PO et rétrospective | Process | — | **à affecter** | 0.5 | | à faire |

**Total estimé : 12.5 h — Total réel : <Y> h**

> ⚠️ **Risque de sur-engagement.** 12,5 h estimées pour une séance de 3 h à 4 personnes
> (12 h de capacité) = **plus de 100 % d'utilisation, sans aucune marge**. Trois options à
> trancher au planning, et à écrire ici :
> 1. prévoir explicitement du travail hors séance (et l'intégrer à la capacité) ;
> 2. sortir une story du sprint (S-03 est la candidate : elle dépend de S-02) ;
> 3. assumer le risque et mesurer l'écart pour corriger l'engagement du sprint 2.
>
> Les trois sont défendables ; ne pas choisir, non.

## 3. Dépendances

- T-13/T-14 (recette) supposent T-10 (modèle ingrédient) : l'ingrédient d'abord.
- T-12 et T-15 (écrans) supposent les API correspondantes, ou alors un travail sur données
  factices à rebrancher ensuite.
- Six tâches sur treize sont encore **sans responsable** : à régler en premier au planning.

## 4. Démo au PO

- Scénario prévu : se connecter → créer 3 ingrédients → créer une recette utilisant ces
  ingrédients → relire la recette.
- Ce que le PO a validé : …
- Ce que le PO a demandé de changer : … *(détail dans `docs/reunions/CR-S1-….md`)*

## 5. Tests

Résultats détaillés : `docs/tests/sprint-1.md`.

| Indicateur | Valeur |
| --- | --- |
| Tests écrits dans le sprint | |
| Tests passants / total | |
| Bugs trouvés / corrigés | |

## 6. Bilan chiffré

| Indicateur | Planifié | Réalisé |
| --- | --- | --- |
| Points | 15 | |
| Heures | 12.5 | |
| Stories terminées | 3 | |

Explication des écarts : …

## 7. Rétrospective

| Ce qui a bien marché | Ce qui a posé problème |
| --- | --- |
| | |

**Actions pour le sprint 2** :

| # | Action | Responsable | Vérifié au sprint 2 |
| --- | --- | --- | --- |
| 1 | | | ☐ |

**Vérification des actions du sprint 0** :

| Action du sprint 0 | Faite ? |
| --- | --- |
| Capacité renseignée pour les sprints 1 à 5 | ☐ |
| Stack actée dans l'ADR 0001 | ☐ |
| Toutes les tâches du sprint ont un responsable | ☐ |
| Protection de `main` activée | ☐ |
| Accès enseignant vérifié (dépôt + board) | ☐ |

## 8. Report au sprint suivant

| Story / tâche | Pourquoi non terminée | Décision |
| --- | --- | --- |
| | | |
