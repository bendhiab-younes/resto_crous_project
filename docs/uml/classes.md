# Diagramme de classes (T-06)

Première version issue du cadrage. À faire évoluer à chaque sprint qui touche au modèle.

```mermaid
classDiagram
    direction LR

    class Utilisateur {
        +int id
        +string identifiant
        +string motDePasseHache
        +Role role
        +verifierMotDePasse(clair) bool
    }

    class Role {
        <<enumeration>>
        CHEF
        INTENDANT
        GESTION_CENTRALE
    }

    class Ingredient {
        +int id
        +string nom
        +string unite
        +float coutParUnite
        +ValeurNutritionnelle nutrition
        +List~Allergene~ allergenes
    }

    class Allergene {
        +int id
        +string nom
    }

    class ValeurNutritionnelle {
        <<value object>>
        +float calories
        +float proteines
        +float glucides
        +float lipides
        +plus(autre, facteur) ValeurNutritionnelle
    }

    class Recette {
        +int id
        +string titre
        +TypePlat type
        +bool vegetarien
        +string procedure
        +StatutRecette statut
        +coutTotal() float
        +nutritionPour100g() ValeurNutritionnelle
        +allergenes() List~Allergene~
        +proposer()
        +valider(intendant)
        +refuser(intendant, motif)
    }

    class LigneRecette {
        +float quantite
        +cout() float
    }

    class StatutRecette {
        <<enumeration>>
        BROUILLON
        A_VALIDER
        VALIDEE
        REFUSEE
    }

    class TypePlat {
        <<enumeration>>
        PROTEINE
        FECULENT
        LEGUME
        VEGETARIEN
    }

    class Menu {
        +int id
        +date jour
        +int semaineCycle
        +coutTotal() float
        +allergenes() List~Allergene~
        +nutritionApprochee() ValeurNutritionnelle
        +estComplet() bool
        +ingredientsManquants() List~Ingredient~
    }

    class LigneMenu {
        +TypePlat emplacement
        +int portions
    }

    class Stock {
        +int id
        +float quantiteDisponible
        +float seuilAlerte
        +estSuffisantPour(quantite) bool
    }

    class Notification {
        +int id
        +string message
        +TypeNotification type
        +datetime creeLe
        +bool lue
        +marquerLue()
    }

    class TypeNotification {
        <<enumeration>>
        STOCK_INSUFFISANT
        RECETTE_A_VALIDER
        CYCLE_NON_RESPECTE
    }

    Utilisateur --> Role
    Utilisateur "1" --> "0..*" Recette : auteur
    Utilisateur "1" --> "0..*" Menu : compose
    Utilisateur "1" --> "0..*" Notification : destinataire

    Recette --> StatutRecette
    Recette --> TypePlat
    Recette "1" *-- "1..*" LigneRecette
    LigneRecette "1" --> "1" Ingredient

    Ingredient "1" --> "1" ValeurNutritionnelle
    Ingredient "0..*" --> "0..*" Allergene
    Ingredient "1" --> "0..1" Stock

    Menu "1" *-- "5" LigneMenu
    LigneMenu "1" --> "1" Recette : recette validée
    LigneMenu --> TypePlat

    Notification --> TypeNotification
```

## Choix de modélisation à justifier dans le rapport

| Choix | Raison |
| --- | --- |
| `ValeurNutritionnelle` en *value object* | Les valeurs nutritionnelles n'ont pas d'identité propre ; on les additionne et on les divise, c'est un calcul, pas une entité |
| `LigneRecette` comme classe d'association | Elle porte la **quantité**, qui n'appartient ni à la recette ni à l'ingrédient seuls |
| `Stock` séparé de `Ingredient` | Le stock est **simulé** et évolue indépendamment de la fiche ingrédient ; on peut le remplacer plus tard par un vrai système |
| Allergènes **dérivés** et non saisis sur la recette | Les allergènes d'une recette sont l'union de ceux de ses ingrédients : les saisir deux fois créerait des incohérences |
| `statut` sur `Recette` | Le workflow de validation (E3) est un état de la recette, pas une entité distincte |
| `Menu` avec 5 `LigneMenu` | Contrainte métier S-09 : 2 protéines, 1 féculent, 1 légume, 1 végétarien — la cardinalité documente la règle, `estComplet()` la vérifie |
