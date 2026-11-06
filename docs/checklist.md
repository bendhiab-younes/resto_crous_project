# Checklist du projet

État au 06/11/2026 : le cadrage est rédigé et le squelette de l'application est en place, mais aucune
story n'est livrée. Cette page dit quoi faire, dans quel ordre et qui s'en charge.

## 1. Calendrier

Chaque séance dure 3 h et le travail se fait pendant les séances : **une séance = un sprint**, soit
12 h de capacité à 4 personnes. Les rituels en prennent environ 1 h par personne.

Les séances du 17/09, du 05/10 et du 13/10 sont passées sans livrable concret. On ne les reconstitue
pas : ce retard est un écart à expliquer dans le rapport et la rétrospective.

Il reste 4 séances, dont la dernière pour clôturer. **Tout le backlog est conservé (68 points)** et
la date de travail retenue est le 17/12, même si le rendu final tombe plus tard. Les stories sont
traitées dans cet ordre, pour avoir au plus tôt le parcours complet ingrédient → recette →
validation → menu du jour :

| Sprint | Séance | Contenu | Pts |
| --- | --- | --- | --- |
| 0 et 1 | 06/11 | Clôture du cadrage, T-22, S-02, S-01 | 10 |
| 2 | 09/11 | Démo au PO, puis S-03, S-04, S-07 | 13 |
| 3 | 10/12 | Démo au PO, puis S-06, S-08, S-09, S-10, S-12 | 16 |
| À placer | selon la vélocité | `Must` : S-05, S-11, S-13 à S-16 | 18 |
| À placer | selon la vélocité | `Should` : S-17 à S-20 | 11 |
| 4 | 17/12 | Démo finale, présentation, rendu | 0 |

**Le risque est assumé.** Le sprint 1 d'origine donne environ 0,7 h par point, soit environ 41 h
pour les 58 points restant après aujourd'hui. Les séances du 09/11 et du 10/12 offrent environ 2 h
de développement par personne, soit 16 h à 4. Il faudra un gain
important grâce à l'IA, du travail hors séance, ou accepter de reporter les dernières stories. La
vélocité mesurée aujourd'hui donnera le vrai écart.

À trancher :

- [ ] **Younes, avec l'enseignant** : peut-on préparer le rapport et la présentation hors séance
      (T-18 à T-21 : 12 h estimées) ?
- [ ] **Avec l'enseignant** : l'autorisation d'utiliser des outils d'IA pour coder.
- [ ] **En équipe** : travailler ou non sur le code hors séance, surtout entre le 09/11 et le 10/12.
      Ces heures entrent alors dans la capacité (`docs/sprints/README.md`).

## 2. Aujourd'hui (06/11)

**Younes**

- [x] Pousser la documentation et la merger dans `main`.
- [x] Ajouter Adam, Aziz et Youssef comme collaborateurs du dépôt.
- [x] Donner accès à l'enseignant : le dépôt et le board sont publics.
- [x] Protéger `main` : PR obligatoire, 1 approbation, revue des Code Owners, contournement possible
      pour Younes.
- [x] Confirmer que Younes code aussi.
- [ ] Corriger `docs/sprints/sprint-0.md` et `docs/reunions/CR-S0-cadrage.md` : garder uniquement ce
      qui s'est réellement passé et remplir les marqueurs.

**Toute l'équipe (30 min en début de séance)**

- [x] Choisir la stack et remplir la section « Décision » de l'ADR 0001.
- [x] Valider le calendrier.
- [ ] Valider la Definition of Done et les rôles.
- [ ] Noter dans le CR l'abandon de Notion pour GitHub Projects, l'approbation des PR par Younes et
      son droit de merger ses propres PR sans relecture.
- [ ] Renseigner la capacité du sprint dans `docs/sprints/sprint-1.md`, et y noter le changement de
      périmètre : S-03 passe au sprint 2.
- [ ] Rédiger le CR de cette réunion le jour même.

**Aziz (T-04)**

- [x] Créer le [board GitHub Projects](https://github.com/users/bendhiab-younes/projects/1), relié
      au dépôt, avec les statuts À faire, En cours, En revue et Terminé.
- [x] Ajouter les champs Sprint, Priorité, Type de tâche, Points, Est. (h), Réel (h).
- [x] Créer une issue par story et par tâche, dont T-22, avec l'identifiant dans le titre.
- [x] Affecter les tâches du sprint 1 selon la répartition validée.
- [x] Rendre le board public pour que l'enseignant y ait accès.
- [ ] Vérifier le board.

**Après la réunion**

- [ ] Mettre à jour `docs/planning-gantt.md`, `docs/sprints/README.md` et la mention de « 5 séances »
      dans `CONTRIBUTING.md` avec le calendrier validé.

## 3. Plan de développement

### Sprint 1 (aujourd'hui) : répartition

| Qui | Tâches | Est. (h) |
| --- | --- | --- |
| Younes | ~~T-22 squelette du projet~~ (terminée) | 1 |
| Youssef | T-07 à T-09 (S-01 connexion) | 2,5 |
| Aziz | T-04 (board), puis T-10, T-11 (S-02 ingrédients) | 3 |
| Adam | Relecture de T-05 et T-06 (première version déjà faite), puis T-12 (écrans ingrédients) | 2 |
| Younes | Relecture des PR, T-17 (revue, CR, rétrospective) | en continu |

T-22 entrera dans `tasks.csv` à la clôture du sprint.

Avec 2,5 h par développeur après la réunion, ce sprint est plein. S-02 passe avant S-01 car il est
sur le chemin critique : si le temps manque, c'est S-01 qui est reporté.

### Sprints suivants

- [ ] **Sprint 2** : découper S-04 et S-07 en tâches au planning du 09/11 (S-03 l'est déjà).
- [ ] **Sprint 3** : découper S-06, S-08, S-09, S-10 et S-12 au planning du 10/12.
- [ ] **Stories à placer** : les intégrer dès que la vélocité le permet, `Must` avant `Should`.
- [ ] **Sprint 4** : démo répétée, présentation, rapport et rapports de tests prêts.

Revoir ce plan à chaque planning à partir de la vélocité réelle.

### Relecture des PR

Younes est le seul à approuver, et il code aussi : il peut bloquer l'équipe sur une séance de 3 h.

- [ ] Relire les PR au fil de la séance, pas à la fin.
- [ ] Garder des PR petites : une tâche par PR.
- [ ] Arrêter d'ouvrir des PR 30 min avant la fin de séance, pour pouvoir tout merger.

### Utilisation de l'IA

- [ ] Claude Code lit `CLAUDE.md`. Avec Copilot, suivre directement `CONTRIBUTING.md`.
- [ ] L'auteur d'une PR doit savoir expliquer son code.
- [ ] Vérifier à la main les résultats attendus des tests de calcul : une IA peut écrire un test qui
      confirme son propre résultat faux.
- [ ] Compter dans les heures réelles le temps passé à relire ce que l'IA a produit.

## 4. À chaque sprint

- [ ] **Planning** : copier `TEMPLATE-sprint.md` en `sprint-N.md`, fixer la capacité, affecter
      chaque tâche avec une estimation en heures.
- [ ] **Démo PO** : en début de séance, rédiger le CR le jour même dans `docs/reunions/`.
- [ ] **Pendant la séance** : reporter les heures réelles, noter les blocages quand ils surviennent.
- [ ] **Tests** : remplir `docs/tests/sprint-N.md` (Youssef).
- [ ] **Modèle modifié** : mettre à jour l'UML dans la même PR (Adam).
- [ ] **Décision technique** : écrire un ADR.
- [ ] **Clôture** : calculer la vélocité (une story à 90 % compte 0 point), faire la rétrospective.
- [ ] **Backlog** : mettre à jour les CSV à partir du board et les commiter (Aziz).

## 5. Rendus

| Rendu | Où | Responsable | État |
| --- | --- | --- | --- |
| Code, historique git, documentation | dépôt | toute l'équipe | à produire |
| UML ou Gantt | `docs/uml/`, `docs/planning-gantt.md` | Adam | première version, Gantt à recaler |
| Sprints et estimations | `docs/sprints/`, `docs/backlog/` | Younes, Aziz | capacité manquante |
| Comptes rendus de réunions | `docs/reunions/` | Younes | CR de cadrage à corriger |
| Rapports de tests | `docs/tests/` | Youssef | template seulement |
| Rétrospective | pages de sprint, puis rapport | Younes | à chaque sprint |
| Rapport final (T-21) | `docs/rapport/` | Adam | plan seulement |
| Scénario de démo (T-19) | `docs/rapport/` | à affecter | avant le 17/12 |
| Présentation finale (T-20, 25 % de la note) | slides | à affecter | avant le 17/12 |

Le rapport s'écrit au fil du projet. L'évaluation récompense surtout la conduite du projet : il
faut y montrer les écarts, dont le démarrage tardif, et ce que l'équipe en a fait.
