# Planning prévisionnel (Gantt)

Planning recalé le 06/11/2026 sur le calendrier réel des séances de 3 h : 17/09, 05/10, 13/10,
06/11, 09/11, 10/12 et 17/12. Le premier planning supposait une séance par semaine à partir du
06/10 ; il reste dans l'historique git. L'écart entre les deux alimentera la rétrospective finale.

Un sprint = une séance de TP, et le travail hors séance décidé par l'équipe compte dans le sprint
qu'il prépare. Les trois premières séances n'ont pas produit de livrable concret.

```mermaid
gantt
    title Gestionnaire de menus et de recettes — planning par sprint
    dateFormat YYYY-MM-DD
    axisFormat %d/%m

    section Sprint 0 — Cadrage
    Cadrage, backlog, dépôt, stack, board (T-01 à T-04) :done, s0, 2026-09-17, 2026-11-06
    Clôture du cadrage                        :milestone, m0, 2026-11-06, 0d

    section Sprint 1 — Connexion et ingrédients
    Squelette du projet (T-22)                :done,    t22, 2026-11-06, 1d
    Ingrédients S-02 (T-10 à T-12)            :active,  s02, 2026-11-06, 2026-11-09
    Authentification S-01 (T-07 à T-09)       :active,  s01, 2026-11-06, 2026-11-09
    Relecture UML (T-05, T-06)                :         t05, 2026-11-06, 2026-11-09
    Démo, CR et rétrospective (T-17)          :milestone, m1, 2026-11-09, 0d

    section Sprint 2 — Recettes, calculs, stock
    Recettes S-03 (T-13 à T-15)               :         s03, 2026-11-09, 2026-12-10
    Tests des API (T-16)                      :         t16, 2026-11-09, 2026-12-10
    Nutrition, allergènes, coût S-04          :         s04, 2026-11-09, 2026-12-10
    Saisie du stock S-07                      :         s07, 2026-11-09, 2026-12-10
    Démo, CR et rétrospective                 :milestone, m2, 2026-12-10, 0d

    section Sprint 3 — Validation et menus
    Proposition de recette S-06               :         s06, 2026-12-10, 2026-12-17
    Validation par l'intendant S-08           :         s08, 2026-12-10, 2026-12-17
    Composition d'un menu S-09, S-10          :         s09, 2026-12-10, 2026-12-17
    Menu du jour S-12                         :         s12, 2026-12-10, 2026-12-17

    section Sprint 4 — Clôture
    Stabilisation et rapport de tests (T-18)  :         t18, 2026-12-10, 2026-12-17
    Démo finale, présentation, rapport (T-19 à T-21) :  t19, 2026-12-10, 2026-12-17
    Rendu et présentation                     :milestone, fin, 2026-12-17, 0d
```

Les stories « à placer » (S-05, S-11, S-13 à S-20 : 29 points) n'ont pas de date : elles entrent
dans un sprint dès que la vélocité le permet, `Must` avant `Should`. Les sprints 3 et 4 se
recouvrent entre le 10/12 et le 17/12 : la séance du 10/12 est la dernière avant la clôture.

## Chemin critique

```
S-02 (ingrédients) → S-03 (recettes) → S-04 (calculs) → S-08 (validation)
                                                      → S-09/S-11 (menus) → S-16 (PDF)
```

Tout part de l'**ingrédient** : c'est lui qui porte le coût, la nutrition et les allergènes dont
dépendent tous les calculs en aval. Un retard sur S-02 décale mécaniquement les sprints 2 et 3.

## Marges et risques

| Risque | Impact | Parade |
| --- | --- | --- |
| Trois séances passées sans livrable | Moins de temps pour 68 points | Travail hors séance, aide de l'IA, report des stories « à placer » |
| 68 points pour environ 16 h de développement en séance | Rendu incomplet | Vélocité mesurée à chaque sprint, périmètre revu au planning |
| Un mois sans séance entre le 09/11 et le 10/12 | Pas de retour du PO pendant le sprint 2 | Travail hors séance planifié, avancement visible sur le board public |
| Younes est le seul à approuver les PR | Équipe bloquée en attente de relecture | PR petites, relues au fil de l'eau |
| Export PDF (S-16) encore « à placer » | Story `Must` non livrée | La prioriser dès que la vélocité le permet |
| Nouvelle demande du PO en cours de projet | Décalage du planning | Les stories `Could` (S-21, S-22) servent de variable d'ajustement |
| Absence d'un membre à une séance | Perte de 25 % de la capacité | Réaffectation en début de séance, notée dans la page de sprint |
