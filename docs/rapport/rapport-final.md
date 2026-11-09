# Rapport final — Gestionnaire de menus et de recettes

> **État du document :** brouillon évolutif de T-21.  
> Le projet étant encore en cours, les informations non présentes dans le dépôt ou le board
> restent explicitement marquées « à renseigner » plutôt que reconstituées.

## 1. Présentation du projet

Le projet consiste à développer un gestionnaire de menus et de recettes pour un restaurant
universitaire. Le produit doit permettre de gérer les ingrédients, créer des recettes, calculer
leur coût, leur nutrition et leurs allergènes, puis les intégrer dans des menus.

Le périmètre prévu comprend également :

- l'authentification et les rôles `CHEF`, `INTENDANT` et `GESTION_CENTRALE` ;
- le workflow de proposition, validation ou refus d'une recette ;
- la simulation du stock ;
- la composition de menus sur un cycle de deux semaines ;
- la consultation du menu du jour par les usagers ;
- l'export PDF des menus et des recettes ;
- une API destinée à un site externe.

L'équipe est composée de Younes Ben Dhiab (Scrum Master, développement, qualité), Adam
Youssef--Muzzi (documentation et modélisation), Aziz Mdallel (outils de suivi et backlog) et
Youssef Essid (tests). L'enseignant joue le rôle de Product Owner.

## 2. Organisation et processus

Le projet est conduit avec Scrum adapté au contexte du TP : une séance correspond à un sprint.
L'équipe utilise GitHub Issues et GitHub Projects pour le backlog, les statuts, les estimations et
les affectations. Le dépôt GitHub constitue la référence du code et de la documentation.

Le workflow retenu impose :

1. une branche par story ou tâche ;
2. un identifiant `S-xx` ou `T-xx` dans la branche, les commits et la pull request ;
3. une pull request vers `main` ;
4. une relecture et une approbation avant le merge ;
5. des tests nominaux et d'erreur pour chaque story livrée ;
6. la mise à jour de la documentation et du board à la clôture du sprint.

La Definition of Done exige notamment que les critères d'acceptation soient satisfaits, que les
tests passent, que le résultat soit consigné et que la story soit démontrable au PO.

## 3. Backlog produit

Le backlog comporte huit epics :

| Epic | Sujet | Priorité |
| --- | --- | --- |
| E1 | Recettes | Must |
| E2 | Menus | Must |
| E3 | Workflow de validation | Must |
| E4 | Stocks (simulation) | Must |
| E5 | Allergènes et nutrition | Must |
| E6 | Notifications | Should |
| E7 | Export et API | Must |
| E8 | Utilisateurs et sécurité | Must |

Il comprend 22 stories, de S-01 à S-22, pour un total de 68 points. Les stories Must portent le
parcours critique ingrédients → recettes → calculs → validation → menus. Les stories S-21 et S-22
restent au backlog avec la priorité `Could`.

Les exports détaillés sont disponibles dans [`docs/backlog/`](../backlog/). Le board GitHub
Projects reste la source de vérité ; les CSV sont des exports à mettre à jour à la clôture des
sprints.

## 4. Modélisation

Les diagrammes Mermaid du projet décrivent :

- les acteurs et cas d'utilisation dans [`docs/uml/cas-usage.md`](../uml/cas-usage.md) ;
- les entités et relations dans [`docs/uml/classes.md`](../uml/classes.md) ;
- le workflow de validation dans [`docs/uml/sequence-validation.md`](../uml/sequence-validation.md).

Les choix structurants sont les suivants :

- les propriétés nutritionnelles, le coût et les allergènes d'une recette sont dérivés de ses
  lignes d'ingrédients ;
- `LigneRecette` porte la quantité et relie une recette à un ingrédient ;
- `Stock` est séparé de `Ingredient` afin de conserver une simulation remplaçable ;
- le statut d'une recette suit le cycle `BROUILLON` → `A_VALIDER` → `VALIDEE` ou `REFUSEE` ;
- un menu complet contient deux protéines, un féculent, un légume et un plat végétarien.

Les diagrammes devront être réactualisés si le modèle évolue pendant les derniers sprints.

## 5. Planification

Le planning initial prévoyait cinq sprints de développement et un sprint de clôture. Le démarrage
tardif a conduit l'équipe à revoir le calendrier et à conserver le backlog complet de 68 points
avec un risque explicitement assumé.

Le chemin critique identifié est :

```text
S-02 ingrédients → S-03 recettes → S-04 calculs → S-08 validation
                                      → S-09/S-11 menus → S-16 PDF
```

Les capacités réellement disponibles, les dates définitives et les écarts de planning sont à
compléter à partir des pages de sprint et du board :

| Élément | Valeur |
| --- | --- |
| Capacité totale réellement disponible | *à renseigner* |
| Date réelle de fin | *à renseigner* |
| Vélocité par sprint | *à renseigner* |
| Écart entre planning prévu et planning réel | *à renseigner* |

## 6. Déroulement des sprints

### Sprint 0 — Cadrage

Le sprint 0 a produit le dépôt, le workflow Git, le backlog initial, le GitHub Project, la
Definition of Done, les rôles, la première modélisation UML et le choix de la stack. Les tâches
T-01 à T-04 sont indiquées comme terminées dans [`docs/sprints/sprint-0.md`](../sprints/sprint-0.md).

Les difficultés constatées sont le démarrage tardif, l'absence initiale de capacité mesurée, le
remplacement de Notion par GitHub Projects et le retard de mise à disposition du dépôt au PO.

### Sprint 1 — Connexion et ingrédients

Le sprint 1 a été recentré sur S-01 et S-02, pour un engagement de 10 points. S-03 a été déplacée
au sprint 2 car elle dépend de S-02 et que la charge initiale dépassait la capacité prévue.

Le squelette T-22, l'authentification, les modèles d'utilisateur et d'ingrédient, le CRUD
d'ingrédients, les écrans de connexion et d'ingrédients ainsi que les calculs de recette sont
présents dans l'historique du dépôt. Le statut exact des stories et la validation du PO doivent
être reportés après la démo :

| Élément | Résultat |
| --- | --- |
| Stories terminées au sens de la Definition of Done | *à renseigner* |
| Vélocité | *à renseigner* |
| Tests exécutés et passants | *à renseigner* |
| Retours du PO | *à renseigner dans le CR* |

### Sprints 2 à 4

Les pages de ces sprints et leurs résultats sont à créer ou à compléter pendant les séances. Elles
devront préciser les stories réellement engagées, les tâches, la démo, les tests, les écarts et la
rétrospective.

## 7. Suivi quantitatif

Les valeurs planifiées proviennent du planning révisé le 06/11 ([`docs/sprints/README.md`](../sprints/README.md)).
Les valeurs réalisées ne doivent pas être déduites des commits : elles doivent venir du board et
des pages de sprint.

| Sprint | Points planifiés | Points réalisés | Heures planifiées | Heures réelles | Vélocité |
| --- | ---: | ---: | ---: | ---: | ---: |
| 0 | 0 | *à renseigner* | *à renseigner* | *à renseigner* | *à renseigner* |
| 1 | 10 | *à renseigner* | *à renseigner* | *à renseigner* | *à renseigner* |
| 2 | 13 | *à renseigner* | *à renseigner* | *à renseigner* | *à renseigner* |
| 3 | 16 | *à renseigner* | *à renseigner* | *à renseigner* | *à renseigner* |
| 4 | 0 | *à renseigner* | *à renseigner* | *à renseigner* | *à renseigner* |

> Le planning initial de l'export [`docs/backlog/sprints.csv`](../backlog/sprints.csv) prévoyait
> 15, 19, 20 et 14 points pour les sprints 1 à 4, puis un sprint 5. Cet écart avec le planning
> révisé le 06/11 doit être expliqué dans le bilan final.

## 8. Réalisation technique

La stack retenue est Python 3.12, FastAPI, SQLAlchemy, SQLite, Jinja2 et pytest. La décision et
ses conséquences sont décrites dans [`docs/adr/0001-choix-de-la-stack.md`](../adr/0001-choix-de-la-stack.md).

L'application est organisée autour de :

- [`app/main.py`](../../app/main.py), qui crée l'application, initialise la base et monte les
  routeurs ;
- [`app/database.py`](../../app/database.py), qui fournit SQLAlchemy, les sessions et l'activation
  des clés étrangères SQLite ;
- [`app/models/`](../../app/models/), qui contient les modèles métier ;
- [`app/routers/`](../../app/routers/), qui porte les parcours HTTP ;
- [`app/templates/`](../../app/templates/), qui contient le front Jinja2 ;
- [`tests/`](../../tests/), qui contient les tests unitaires et d'intégration.

Les premières difficultés techniques ont porté sur la gestion des sessions serveur, la validation
des formulaires, la protection des pages et la conservation des données saisies lors d'une erreur.
Les difficultés et corrections restantes devront être ajoutées à partir des rapports de tests.

## 9. Tests et qualité

La stratégie prévoit trois niveaux :

1. tests unitaires des calculs métier ;
2. tests d'intégration des routes et de la persistance ;
3. tests manuels des scénarios présentés au PO.

Les tests automatisés sont nommés avec les identifiants `TC-Sxx-yy`. Les résultats détaillés
doivent être consignés dans un rapport par sprint sous [`docs/tests/`](../tests/).

À la date de rédaction, la consolidation suivante reste à produire :

| Indicateur | Valeur |
| --- | --- |
| Nombre total de tests | *à renseigner après `pytest -v`* |
| Tests réussis | *à renseigner* |
| Tests échoués | *à renseigner* |
| Bugs corrigés | *à renseigner* |
| Couverture mesurée | *à renseigner ou indiquer non mesurée* |
| Dette de test acceptée | *à renseigner* |

## 10. Rétrospective globale

### Ce qui a fonctionné

- Le backlog initial a été structuré avec des epics, stories, priorités et estimations.
- Les règles Git et la Definition of Done ont été écrites avant l'accélération du développement.
- Le chemin critique métier a été identifié et a guidé le déplacement de S-03.
- GitHub Projects relie désormais les tâches, les statuts et les pull requests au dépôt.
- La stack retenue limite la configuration et permet de partager une base de code unique.

### Ce qui a posé problème

- Le projet a démarré tardivement et plusieurs séances n'ont pas produit de livrable.
- La capacité réelle n'a pas été mesurée assez tôt.
- Le premier engagement du sprint 1 dépassait la capacité disponible.
- Plusieurs tâches ont d'abord été créées sans responsable.
- Les comptes rendus, rapports de tests et heures réelles restent à tenir au fil des séances.

### Leçons retenues

1. Mesurer la capacité avant d'engager les stories permet d'éviter un sprint sans marge.
2. Découper les stories en tâches affectées rend les blocages visibles plus tôt.
3. Le chemin critique doit guider les priorités lorsque le temps est limité.
4. Les retours du PO, les heures et les résultats de tests doivent être consignés le jour même.
5. Une Definition of Done utile doit être appliquée au board, au code et à la documentation.

### Actions d'amélioration

| Action | Responsable | Échéance | Statut |
| --- | --- | --- | --- |
| Renseigner les heures réelles dans le board et les pages de sprint | *à confirmer* | *à renseigner* | à faire |
| Produire un rapport de tests pour chaque sprint | Youssef Essid | *à renseigner* | à faire |
| Consigner chaque démo et décision du PO dans un CR | *à confirmer* | à chaque sprint | en cours |
| Recalculer la vélocité avant chaque nouvel engagement | Scrum Master | chaque planning | à faire |

## 11. Perspectives

Les perspectives dépendent de la vélocité réellement obtenue et de la validation du PO.

Les fonctionnalités prioritaires encore prévues sont la validation selon le stock, la composition
des menus, le cycle de deux semaines, le menu du jour, les allergènes et les exports PDF.

Les stories suivantes restent explicitement hors engagement à ce stade :

- S-21 — alerte de non-respect du cycle (`Could`) ;
- S-22 — API des menus pour un site externe (`Could`).

Si le projet continuait après la clôture, il faudrait également renforcer la couverture des rôles,
ajouter des migrations de base de données, automatiser davantage la vérification du workflow et
préparer l'API externe à partir d'un contrat versionné.

## Annexes

- Backlog : [`docs/backlog/`](../backlog/)
- UML : [`docs/uml/`](../uml/)
- Planning : [`docs/planning-gantt.md`](../planning-gantt.md)
- Sprints : [`docs/sprints/`](../sprints/)
- Comptes rendus : [`docs/reunions/`](../reunions/)
- Tests : [`docs/tests/`](../tests/)
- Workflow Git : [`CONTRIBUTING.md`](../../CONTRIBUTING.md)
