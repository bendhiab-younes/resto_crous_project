# Diagramme de cas d'usage (T-05)

## Acteurs

| Acteur | Description |
| --- | --- |
| **Chef de cuisine** | Crée des recettes et les propose à la validation ; consulte les recettes validées |
| **Intendant** | Saisit le stock, valide ou refuse les recettes, compose et publie les menus |
| **Gestion centrale** | Administre les utilisateurs et les rôles, supervise les coûts |
| **Usager** | Consulte le menu du jour, les allergènes et la nutrition (sans compte) |
| **Site externe** | Acteur secondaire (système) : consomme l'API des menus |

```mermaid
flowchart LR
    chef(("Chef<br/>de cuisine"))
    intendant(("Intendant"))
    centrale(("Gestion<br/>centrale"))
    usager(("Usager"))
    externe(("Site externe<br/>(système)"))

    subgraph SYS["Gestionnaire de menus et de recettes"]
        direction TB
        UC1["S'authentifier"]
        UC2["Gérer les ingrédients"]
        UC3["Créer une recette"]
        UC4["Consulter nutrition,<br/>allergènes et coût"]
        UC5["Proposer une recette<br/>à la validation"]
        UC6["Valider ou refuser<br/>une recette"]
        UC7["Saisir le stock<br/>des ingrédients"]
        UC8["Composer un menu"]
        UC9["Planifier un menu<br/>sur le cycle de 2 semaines"]
        UC10["Consulter le menu du jour"]
        UC11["Exporter en PDF"]
        UC12["Gérer les utilisateurs<br/>et les rôles"]
        UC13["Consulter<br/>les notifications"]
        UC14["Consulter l'API<br/>des menus"]
    end

    chef --- UC1
    chef --- UC2
    chef --- UC3
    chef --- UC5
    chef --- UC4
    chef --- UC11
    chef --- UC13

    intendant --- UC1
    intendant --- UC6
    intendant --- UC7
    intendant --- UC8
    intendant --- UC9
    intendant --- UC11
    intendant --- UC13
    intendant --- UC4

    centrale --- UC1
    centrale --- UC12
    centrale --- UC4

    usager --- UC10
    usager --- UC4

    externe --- UC14

    UC3 -.->|"«include»"| UC4
    UC6 -.->|"«include»"| UC4
    UC8 -.->|"«include»"| UC4
    UC8 -.->|"«include»"| UC9
    UC6 -.->|"«include»"| UC7
```

## Relations notables

| Relation | Signification |
| --- | --- |
| `UC6 «include» UC7` | Valider une recette suppose de connaître le stock disponible |
| `UC8 «include» UC4` | Composer un menu s'appuie sur le coût et les allergènes des recettes |
| `UC8` → recettes validées uniquement | Règle métier de la story S-10 : une recette non validée n'est pas utilisable dans un menu |

## Règles métier rattachées

1. Un menu contient **2 protéines, 1 féculent, 1 légume et 1 plat végétarien** (S-09).
2. Les menus tournent sur un **cycle de 2 semaines** (S-11).
3. Seules les **recettes validées** entrent dans un menu (S-10).
4. Une recette est refusée si un de ses ingrédients est **indisponible en stock** (S-08).
5. Le **menu du jour** et ses allergènes sont consultables **sans authentification** (S-12, S-15).
