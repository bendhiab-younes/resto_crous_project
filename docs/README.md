# Documentation du projet

Index de toute la documentation. Le dépôt est la **référence unique** pour les rendus : ce qui
n'est pas ici (ou exporté ici depuis le board GitHub Projects) n'existe pas pour l'évaluation.

## Conduite du projet

| Document | Contenu |
| --- | --- |
| [`backlog/`](backlog/) | Epics, user stories, sprints, tâches — export CSV du board GitHub Projects |
| [`github-project.md`](github-project.md) | Configuration et règles d'utilisation du GitHub Project |
| [`checklist.md`](checklist.md) | Ce qu'il reste à faire : calendrier, plan de développement, rendus |
| [`sprints/`](sprints/) | Une page par sprint : objectif, engagement, tâches, vélocité, rétrospective |
| [`reunions/`](reunions/) | Comptes rendus de réunions (PO et internes) |
| [`definition-of-done.md`](definition-of-done.md) | Critères de « terminé » et Definition of Ready |
| [`roles.md`](roles.md) | Rôles Scrum et responsabilités transverses |
| [`planning-gantt.md`](planning-gantt.md) | Planning prévisionnel, chemin critique, risques |
| [`guide-demarrage.md`](guide-demarrage.md) | Installer le projet, savoir qui fait quoi, livrer une tâche |
| [`../CONTRIBUTING.md`](../CONTRIBUTING.md) | Workflow git, conventions, revue de code |

## Technique

| Document | Contenu |
| --- | --- |
| [`uml/`](uml/) | Cas d'usage, classes, séquence du workflow de validation |
| [`adr/`](adr/) | Décisions d'architecture (ADR) |
| [`tests/`](tests/) | Stratégie de test et rapports par sprint |

## Rendu final

| Document | Contenu |
| --- | --- |
| [`rapport/plan-du-rapport.md`](rapport/plan-du-rapport.md) | Plan du rapport et correspondance rendu → source |

## Correspondance rendus attendus → livrables

| Rendu attendu | Où il se trouve | État |
| --- | --- | --- |
| Code + git + documentation | dépôt, `CONTRIBUTING.md`, `docs/` | à produire à partir du sprint 1 |
| Rapport | `docs/rapport/` | plan posé, rédaction en sprint 5 |
| Modélisation UML ou Gantt | `docs/uml/`, `docs/planning-gantt.md` | première version faite |
| Rapports de tests | `docs/tests/` | template prêt, un rapport par sprint |
| Comptes rendus de réunions | `docs/reunions/` | template + CR de cadrage |
| Définition des sprints et estimations | `docs/sprints/`, `docs/backlog/` | faits (capacité à renseigner) |
| Rétrospective du projet | rétros de sprint + `docs/rapport/` | par sprint, consolidée en sprint 5 |
| Démo | `docs/rapport/` (scénario, T-19) | à écrire en sprint 5 |

## Conventions d'écriture

- Un document par sujet, nommé en kebab-case, en **français**.
- Les documents de suivi (CR, pages de sprint, rapports de tests) sont remplis **pendant** la
  séance concernée, jamais reconstitués après coup.
- Les templates (`TEMPLATE-*.md`) ne sont pas modifiés directement : on les **copie**.
- Tout document est référencé depuis cet index.
