# Sprint 1 — Connexion et ingrédients — 06/11/2026

- **Objectif du sprint** : un utilisateur peut se connecter et saisir des ingrédients. C'est la base
  de tout le reste du produit.
- **Scrum Master du sprint** : Younes Ben Dhiab
- **Capacité** : 4 × 3 h = **12 h**, plus les heures hors séance avant le 09/11 *(à renseigner)*
- **Engagement** : 10 points

## 1. Stories engagées

| Story | Intitulé | Pts | Responsable | Statut en fin de sprint |
| --- | --- | --- | --- | --- |
| S-01 | Authentification de l'utilisateur | 5 | Younes Ben Dhiab | |
| S-02 | Gestion des ingrédients (allergènes, nutrition, coût) | 5 | Younes Ben Dhiab | |

**Total engagé : 10 pts — Vélocité : <V> pts**

S-03 (5 pts), prévue au départ, passe au sprint 2 : les séances passées sans livrable ont réduit le
temps disponible, et S-03 dépend de S-02.

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

## 2. Tâches

| Tâche | Intitulé | Type | Story | Assigné | Est. (h) | Réel (h) | Statut |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T-05 | Diagramme de cas d'usage | Doc | — | Adam Youssef--Muzzi | 0.5 | | à faire |
| T-06 | Diagramme de classes | Doc | — | Adam Youssef--Muzzi | 1 | | à faire |
| T-07 | Modèle User + hash du mot de passe | Dev | S-01 | Younes Ben Dhiab | 1 | | à faire |
| T-08 | Endpoints login/logout | Dev | S-01 | Younes Ben Dhiab | 1 | | à faire |
| T-09 | Page de connexion | Dev | S-01 | Adam Youssef--Muzzi | 0.5 | | à faire |
| T-10 | Modèle Ingrédient + migration | Dev | S-02 | Younes Ben Dhiab | 0.5 | | à faire |
| T-11 | CRUD API ingrédients | Dev | S-02 | Younes Ben Dhiab | 1 | | à faire |
| T-12 | Écrans liste et formulaire d'ingrédients | Dev | S-02 | Adam Youssef--Muzzi | 1.5 | | à faire |
| T-17 | Revue de sprint, CR PO et rétrospective | Process | — | Younes Ben Dhiab | 0.5 | | à faire |
| T-22 | Squelette du projet | Setup | — | Younes Ben Dhiab | 1 | | fait |
| T-23 | Calculs de recette (coût, nutrition, allergènes) | Dev | S-04 | Youssef Essid | à estimer | | à faire |
| T-24 | Export PDF de la recette | Dev | S-17 | Aziz Mdallel | à estimer | | à faire |

**Total estimé : 8.5 h, plus T-23 et T-24 à estimer — Total réel : <Y> h**

**Répartition modifiée le 08/11.** Younes prend le code du chemin critique (S-01, S-02, puis S-03).
Les autres reçoivent des tâches indépendantes, chacune sur sa branche, du moins technique au plus
technique : Adam les pages (T-09, T-12, T-15), Youssef les calculs (T-23), Aziz l'export PDF (T-24).
Chaque issue décrit le contrat à respecter (champs, variables de template, signatures), et toutes
les quantités sont en grammes. T-23 et T-24 avancent sur des stories des sprints suivants : leurs
points comptent dans le sprint où la story est terminée.

Le plan d'origine (12,5 h pour 12 h de capacité) dépassait la capacité. L'équipe a choisi de sortir
S-03 du sprint : T-13 à T-16 passent au sprint 2. T-16 couvrant les tests de S-02, ces tests sont
écrits avec T-11 pour que S-02 respecte la Definition of Done.

## 3. Dépendances

- Tout le développement suppose T-22 (squelette du projet), terminée.
- Les pages (T-09, T-12) et les tâches en avance (T-23, T-24) ne dépendent que des contrats écrits
  dans leurs issues ; Younes les branche sur ses routes au moment du merge.
- Si le temps manque, S-01 est reporté plutôt que S-02, qui est sur le chemin critique.

## 4. Démo au PO

- Scénario prévu le 09/11 : se connecter → créer 3 ingrédients → les modifier → les relire.
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
| Points | 10 | |
| Heures | 8.5 | |
| Stories terminées | 2 | |

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
| Capacité renseignée pour les sprints 1 à 5 | ☑ |
| Stack actée dans l'ADR 0001 | ☑ |
| Toutes les tâches du sprint ont un responsable | ☑ |
| Protection de `main` activée | ☑ |
| Accès enseignant vérifié (dépôt + board) | ☑ |

## 8. Report au sprint suivant

| Story / tâche | Pourquoi non terminée | Décision |
| --- | --- | --- |
| S-03, T-13 à T-16 | Sorties du sprint au planning | reportées au sprint 2 |
