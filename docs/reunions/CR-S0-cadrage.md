# CR — Réunion de cadrage interne — Sprint 0 — <JJ/MM/AAAA>

- **Type** : réunion interne de cadrage (sans le PO)
- **Date et durée** : <JJ/MM/AAAA>, <durée>
- **Présents** : Younes Ben Dhiab, Adam Youssef--Muzzi, Aziz Mdallel, Youssef Essid
- **Animateur** : <nom> — **Rédacteur du CR** : <nom>

> ⚠️ Compte rendu à compléter/corriger par l'équipe : les éléments ci-dessous reprennent ce qui
> a effectivement été fait (dépôt créé et partagé, backlog rédigé, stack pressentie) ; les dates,
> noms et horaires restent à renseigner.

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
| 2 | Dépôt GitHub public créé et partagé avec l'enseignant | fait |
| 3 | Workflow git : `main` protégée, une branche par story, PR avec une relecture | documenté dans `CONTRIBUTING.md` |
| 4 | Suivi du projet sur Notion, partagé avec l'enseignant, avec export commité dans `docs/backlog/` | à confirmer (T-04) |
| 5 | Stack pressentie : Python + FastAPI + SQLite | **à acter** — voir `docs/adr/0001-choix-de-la-stack.md` |
| 6 | Backlog initial rédigé : 8 epics, 22 user stories estimées, réparties sur 5 sprints | fait |

## 3. Points ouverts

| # | Question | Qui traite | Pour quand |
| --- | --- | --- | --- |
| 1 | Acter la décision de stack et remplir la section « Décision » de l'ADR 0001 | toute l'équipe | sprint 1 |
| 2 | Confirmer les responsabilités transverses de chacun (Scrum Master : Younes Ben Dhiab) | toute l'équipe | sprint 1 |
| 3 | Renseigner la **capacité en heures** par sprint (indispensable pour comparer planifié / réalisé) | Scrum Master | sprint 1 |
| 4 | Vérifier que l'enseignant a bien accès au dépôt **et** au board Notion | Aziz Mdallel | sprint 1 |
| 5 | Affecter les tâches T-07 à T-11, T-13, T-14, T-16 (sans responsable à ce jour) | toute l'équipe | sprint 1 |

## 4. Actions

| # | Action | Responsable | Échéance | Statut |
| --- | --- | --- | --- | --- |
| 1 | Créer `/docs`, `.gitignore`, README, CONTRIBUTING, templates (T-01) | Adam, Younes | sprint 0 | fait |
| 2 | Activer la protection de branche sur `main` dans GitHub | Adam | sprint 0 | à faire |
| 3 | Rédiger l'ADR de stack et le comparatif (T-02) | toute l'équipe | sprint 0 | fait (décision à acter) |
| 4 | Rédiger la DoD et répartir les rôles (T-03) | Younes | sprint 0 | fait (rôles à confirmer) |
| 5 | Structurer Notion et donner l'accès au PO (T-04) | Aziz Mdallel | sprint 0 | à faire |

## 5. Contenu du sprint 1

- **Objectif** : connexion, gestion des ingrédients, création de recettes.
- **Stories engagées** : S-01 (5 pts), S-02 (5 pts), S-03 (5 pts) — **total : 15 pts**.
- À présenter au PO en début de séance 1 : le backlog, pour validation des priorités.
