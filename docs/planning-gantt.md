# Planning prévisionnel (Gantt)

> ⚠️ **Dates à ajuster** : les dates ci-dessous supposent une séance de TP par semaine à partir
> du 6 octobre 2026. Remplacer par les dates réelles des séances dès qu'elles sont connues —
> c'est l'écart entre ce planning et la réalité qui alimentera la rétrospective finale.

Un sprint = une séance de TP. Les tâches de documentation et de gestion de projet courent en
parallèle du développement et ne sont donc pas des jalons isolés.

```mermaid
gantt
    title Gestionnaire de menus et de recettes — planning par sprint
    dateFormat YYYY-MM-DD
    axisFormat %d/%m
    excludes weekends

    section Sprint 0 — Cadrage
    Dépôt git et workflow (T-01)              :done,    t01, 2026-10-06, 2d
    Choix de la stack et ADR (T-02)           :active,  t02, 2026-10-06, 3d
    Definition of Done et rôles (T-03)        :active,  t03, 2026-10-07, 2d
    Outil de suivi et accès PO (T-04)         :         t04, 2026-10-08, 2d
    Rédaction du backlog initial              :done,    bk0, 2026-10-06, 3d

    section Sprint 1 — Base du produit
    Modélisation UML (T-05, T-06)             :         t05, 2026-10-13, 2d
    Authentification S-01 (T-07 à T-09)       :         s01, 2026-10-13, 3d
    Ingrédients S-02 (T-10 à T-12)            :         s02, 2026-10-13, 3d
    Recettes S-03 (T-13 à T-15)               :         s03, after s02, 3d
    Tests API (T-16)                          :         t16, after s03, 1d
    Démo, CR et rétrospective (T-17)          :milestone, m1, 2026-10-19, 0d

    section Sprint 2 — Calculs et validation
    Nutrition, allergènes, coût S-04          :         s04, 2026-10-20, 3d
    Rôles et droits S-05                      :         s05, 2026-10-20, 2d
    Proposition de recette S-06               :         s06, 2026-10-22, 2d
    Saisie du stock S-07                      :         s07, 2026-10-22, 2d
    Validation par l'intendant S-08           :         s08, after s07, 3d
    Démo, CR et rétrospective                 :milestone, m2, 2026-10-26, 0d

    section Sprint 3 — Menus
    Composition d'un menu S-09                :         s09, 2026-11-03, 3d
    Recettes validées uniquement S-10         :         s10, 2026-11-03, 1d
    Cycle de 2 semaines S-11                  :         s11, after s09, 3d
    Menu du jour S-12                         :         s12, 2026-11-05, 2d
    Coût du menu S-13                         :         s13, 2026-11-05, 1d
    Alerte de stock S-14                      :         s14, after s11, 2d
    Allergènes du menu S-15                   :         s15, 2026-11-06, 1d
    Démo, CR et rétrospective                 :milestone, m3, 2026-11-09, 0d

    section Sprint 4 — Export et confort
    Export PDF du menu S-16                   :         s16, 2026-11-10, 2d
    Export PDF de la recette S-17             :         s17, after s16, 2d
    Coût et allergènes en validation S-18     :         s18, 2026-11-10, 1d
    Nutrition du menu S-19                    :         s19, 2026-11-12, 2d
    Centre de notifications S-20              :         s20, 2026-11-12, 2d
    Stabilisation et rapport de tests (T-18)  :         t18, after s19, 2d
    Démo, CR et rétrospective                 :milestone, m4, 2026-11-16, 0d

    section Sprint 5 — Clôture
    Scénario et répétition de la démo (T-19)  :         t19, 2026-11-17, 2d
    Présentation finale (T-20)                :         t20, 2026-11-17, 3d
    Rapport final et rétrospective (T-21)     :         t21, 2026-11-17, 4d
    Rendu et présentation                     :milestone, fin, 2026-11-23, 0d
```

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
| Sprint 1 planifié à ~104 % de la capacité | Report de S-03 | Sortir S-03 ou prévoir du travail hors séance (décision au planning) |
| Nouvelle demande du PO en cours de projet | Décalage du planning | Les stories `Could` (S-21, S-22) servent de variable d'ajustement |
| Export PDF sous-estimé (sprint 4) | Rendu incomplet | Prototyper l'export dès le sprint 3 sur une recette |
| Absence d'un membre à une séance | Perte de 25 % de la capacité | Réaffectation en début de séance, notée dans la page de sprint |
