# Sprint 0 — Cadrage — <JJ/MM/AAAA>

- **Objectif du sprint** : être prêt à développer dès le sprint 1 — dépôt, règles d'équipe,
  outil de suivi, backlog initial, stack.
- **Scrum Master du sprint** : <nom>
- **Capacité** : <nb membres> × <heures> = **<X> h** *(à renseigner)*
- **Engagement** : 0 point (sprint de mise en place, aucune story produit)

## 1. Stories engagées

Aucune : le sprint 0 ne produit pas de fonctionnalité. Il produit le **cadre** qui rend les
sprints suivants mesurables.

## 2. Tâches

| Tâche | Intitulé | Type | Assigné | Est. (h) | Réel (h) | Statut |
| --- | --- | --- | --- | --- | --- | --- |
| T-01 | Dépôt GitHub public + workflow git (branches, PR) | Setup | Adam Youssef--Muzzi, Younes Ben Dhiab | 1 | | en cours |
| T-02 | Choix de la stack + ADR | Setup | Toute l'équipe | 1.5 | | en cours (décision à acter) |
| T-03 | Definition of Done + répartition des rôles | Process | Younes Ben Dhiab | 1 | | en cours (rôles à confirmer) |
| T-04 | Structurer le board GitHub Projects et donner l'accès au PO | Setup | Aziz Mdallel | 1.5 | | à faire |

**Total estimé : 5 h — Total réel : <Y> h**

### Détail de T-01

| Sous-élément | Statut |
| --- | --- |
| Dépôt public créé et partagé avec l'enseignant | fait |
| `README.md` décrivant le produit, l'équipe et la documentation | fait |
| `.gitignore` | fait |
| Dossier `/docs` structuré | fait |
| `CONTRIBUTING.md` : nommage des branches, commits, revue | fait |
| Template de pull request | fait |
| **Protection de la branche `main` activée dans GitHub** | **à faire** |

## 3. Livrables du sprint

- `README.md`, `.gitignore`, `CONTRIBUTING.md`, `.github/pull_request_template.md`
- `docs/adr/0001-choix-de-la-stack.md` (comparatif des options, décision à acter)
- `docs/definition-of-done.md`, `docs/roles.md`
- `docs/backlog/` : epics, stories, sprints, tâches (export en format ouvert)
- `docs/uml/` : diagrammes de cas d'usage et de classes (première version)
- `docs/planning-gantt.md`
- Templates : CR de réunion, page de sprint, rapport de tests

## 4. Démo au PO

Pas de démo produit. À présenter en début de séance 1 : le backlog (epics, stories, priorités
MoSCoW) pour **validation des priorités par le PO** — c'est lui qui décide de l'ordre.

## 5. Bilan chiffré

| Indicateur | Planifié | Réalisé |
| --- | --- | --- |
| Points | 0 | 0 |
| Heures | 5 | <Y> |
| Tâches terminées | 4 | <n> |

## 6. Rétrospective

| Ce qui a bien marché | Ce qui a posé problème |
| --- | --- |
| Backlog rédigé de bout en bout (8 epics, 22 stories estimées) dès le cadrage | Capacité en heures non renseignée : impossible de vérifier que le sprint 1 est réaliste |
| Thème validé et dépôt partagé avec l'enseignant sans friction | Plusieurs tâches de développement sans responsable désigné |
| Règles git écrites avant la première ligne de code | Décision de stack non actée formellement malgré le comparatif |

**Actions pour le sprint 1** :

| # | Action | Responsable | Vérifié au sprint 1 |
| --- | --- | --- | --- |
| 1 | Renseigner la capacité (h) des sprints 1 à 5 | Scrum Master | ☐ |
| 2 | Acter la stack et remplir la section « Décision » de l'ADR 0001 | Toute l'équipe | ☐ |
| 3 | Affecter un responsable à chaque tâche du sprint 1 | Scrum Master | ☐ |
| 4 | Activer la protection de `main` sur GitHub | Adam | ☐ |
| 5 | Vérifier l'accès de l'enseignant au dépôt et au board | Aziz Mdallel | ☐ |

## 7. Report au sprint suivant

| Tâche | Pourquoi non terminée | Décision |
| --- | --- | --- |
| T-02 (décision) | Comparatif prêt, décision collective non prise | à acter en début de sprint 1 |
| T-04 | Board à structurer et à partager | reportée en sprint 1 |
