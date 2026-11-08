# CR — Réunion de cadrage interne — Sprint 0 — <JJ/MM/AAAA>

- **Type** : réunion interne de cadrage (sans le PO)
- **Date et durée** : <JJ/MM/AAAA>, <durée>
- **Présents** : Younes Ben Dhiab, Adam Youssef--Muzzi, Aziz Mdallel, Youssef Essid
- **Animateur** : <nom> — **Rédacteur du CR** : <nom>

> Compte rendu corrigé le 06/11/2026 : les statuts reflètent ce qui a réellement été fait, avec la
> date quand ils ont changé après la réunion. Suite dans [`CR-S1-planning.md`](CR-S1-planning.md).

## 1. Ordre du jour

1. Choix du thème de projet et validation auprès de l'enseignant.
2. Mise en place du dépôt et du workflow git (T-01).
3. Choix de la stack (T-02).
4. Definition of Done et répartition des rôles (T-03).
5. Mise en place de l'outil de suivi et accès PO (T-04).
6. Première rédaction du backlog (epics, stories, estimations).

## 2. Décisions prises

| # | Décision | Statut |
| --- | --- | --- |
| 1 | Thème retenu : **gestionnaire de menus et de recettes** (sujet 10), un seul groupe par thème | fait |
| 2 | Dépôt GitHub public créé et partagé avec l'enseignant | fait le 06/11 : le dépôt était privé jusque-là |
| 3 | Workflow git : `main` protégée, une branche par story, PR avec une relecture | documenté dans `CONTRIBUTING.md`, protection activée le 06/11 |
| 4 | Suivi du projet sur Notion, partagé avec l'enseignant, avec export commité dans `docs/backlog/` | abandonné le 06/11 : Notion devenu payant, remplacé par GitHub Projects |
| 5 | Stack pressentie : Python + FastAPI + SQLite | acté le 06/11 — voir `docs/adr/0001-choix-de-la-stack.md` |
| 6 | Backlog initial rédigé : 8 epics, 22 user stories estimées, réparties sur 5 sprints | fait |

## 3. Points ouverts

| # | Question | Qui traite | Pour quand |
| --- | --- | --- | --- |
| 1 | Acter la décision de stack et remplir la section « Décision » de l'ADR 0001 | toute l'équipe | traité le 06/11 |
| 2 | Confirmer les responsabilités transverses de chacun (Scrum Master : Younes Ben Dhiab) | toute l'équipe | traité le 06/11 |
| 3 | Renseigner la **capacité en heures** par sprint (indispensable pour comparer planifié / réalisé) | Scrum Master | traité le 06/11 : 12 h par sprint |
| 4 | Vérifier que l'enseignant a bien accès au dépôt **et** au board | Aziz Mdallel | traité le 06/11 : dépôt et board publics |
| 5 | Affecter les tâches T-07 à T-11, T-13, T-14, T-16 (sans responsable à ce jour) | toute l'équipe | T-07 à T-11 traitées le 06/11, reste T-13, T-14, T-16 |

## 4. Actions

| # | Action | Responsable | Échéance | Statut |
| --- | --- | --- | --- | --- |
| 1 | Créer `/docs`, `.gitignore`, README, CONTRIBUTING, templates (T-01) | Adam, Younes | sprint 0 | fait |
| 2 | Activer la protection de branche sur `main` dans GitHub | Younes | sprint 0 | fait le 06/11 |
| 3 | Rédiger l'ADR de stack et le comparatif (T-02) | toute l'équipe | sprint 0 | fait le 06/11 |
| 4 | Rédiger la DoD et répartir les rôles (T-03) | Younes | sprint 0 | fait le 06/11 |
| 5 | Structurer le board et donner l'accès au PO (T-04) | Aziz Mdallel | sprint 0 | fait le 06/11, sur GitHub Projects |

## 5. Contenu du sprint 1

- **Objectif prévu** : connexion, gestion des ingrédients, création de recettes.
- **Stories prévues** : S-01 (5 pts), S-02 (5 pts), S-03 (5 pts) — **total : 15 pts**.
- **Corrigé le 06/11** : S-03 passe au sprint 2, le sprint 1 porte sur 10 pts.
- À présenter au PO : le backlog, pour validation des priorités (prévu le 09/11).
