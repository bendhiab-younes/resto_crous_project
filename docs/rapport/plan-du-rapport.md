# Plan du rapport final (T-21)

Le rapport est **rédigé au fil du projet**, pas en sprint 5 : chaque section s'alimente des
documents déjà produits. Cette page liste, pour chaque section, sa **source dans le dépôt** —
rédiger consiste alors à synthétiser et commenter, pas à retrouver l'information.

| # | Section | Contenu | Source dans le dépôt |
| --- | --- | --- | --- |
| 1 | Présentation du projet | Thème, besoin du client, périmètre, équipe et rôles | `README.md`, `docs/roles.md` |
| 2 | Organisation et processus | Scrum adapté au TP, rituels, outils de suivi, workflow git | `CONTRIBUTING.md`, `docs/definition-of-done.md` |
| 3 | Backlog produit | Epics, user stories, priorisation MoSCoW, estimation en points | `docs/backlog/` |
| 4 | Modélisation | Cas d'usage, classes, séquence + justification des choix | `docs/uml/` |
| 5 | Planification | Gantt, chemin critique, capacité par sprint, risques | `docs/planning-gantt.md`, `docs/sprints/` |
| 6 | Déroulement sprint par sprint | Pour chaque sprint : objectif, livré, démo, écarts, décisions du PO | `docs/sprints/`, `docs/reunions/` |
| 7 | Suivi quantitatif | Planifié / réalisé en points et en heures, vélocité, qualité des estimations | `docs/backlog/sprints.csv`, pages de sprint |
| 8 | Réalisation technique | Architecture, stack et sa justification, principales difficultés techniques | `docs/adr/`, code |
| 9 | Tests et qualité | Stratégie, résultats par sprint, anomalies, dette de test assumée | `docs/tests/` |
| 10 | Rétrospective globale | Difficultés rencontrées, leçons tirées, ce qu'on ferait autrement | rétros de sprint (section 6 des pages de sprint) |
| 11 | Perspectives | Fonctionnalités non réalisées, évolutions envisagées si le projet continuait | stories `Could` restées au backlog, `docs/backlog/stories.csv` |
| — | Annexes | CR de réunions, rapports de tests complets, export du backlog | `docs/reunions/`, `docs/tests/`, `docs/backlog/` |

## Ce que l'évaluation récompense

Le sujet est explicite : *« ces TP visent avant tout à mettre en application des concepts,
méthodes et outils visant à la bonne conduite d'un projet de développement logiciel, et ce seront
donc principalement ces aspects qui seront récompensés plus que les productions techniques. »*

Conséquence pour la rédaction : les sections 2, 6, 7 et 10 sont le cœur du rapport. On y
privilégie **les écarts et ce qu'on en a fait** plutôt que le récit d'un projet lisse — un
sprint mal estimé, analysé puis corrigé au sprint suivant, démontre mieux la maîtrise du process
qu'un planning prétendument respecté.

## Matière à collecter en continu (sinon elle est perdue)

| Élément | Quand le noter | Où |
| --- | --- | --- |
| Heures réellement passées par tâche | à la fin de chaque tâche | board + page de sprint |
| Demandes et changements d'avis du PO | pendant la réunion | CR de réunion |
| Difficultés et blocages | le jour où ils surviennent | rétro de la page de sprint |
| Décisions techniques et leurs raisons | au moment de décider | ADR |
| Résultats de tests et bugs | à chaque exécution de la suite | `docs/tests/sprint-N.md` |

## Plan de la présentation finale (T-20, 25 % de la note)

1. Le produit en 1 slide : à qui il sert, ce qu'il fait.
2. **Démo de bout en bout** (scénario écrit et répété — T-19).
3. Organisation de l'équipe et process effectivement appliqué.
4. Chiffres : vélocité par sprint, planifié vs réalisé, couverture de tests.
5. Difficultés rencontrées et comment on les a traitées.
6. Leçons tirées (individuelles et collectives).
7. Perspectives : ce qu'on ferait au sprint 6.
