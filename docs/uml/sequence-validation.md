# Diagramme de séquence — Workflow de validation d'une recette

Couvre les stories **S-06** (le chef propose) et **S-08** (l'intendant valide ou refuse selon
le stock), avec la notification **S-14**.

```mermaid
sequenceDiagram
    actor Chef
    actor Intendant
    participant App as Application
    participant Recette
    participant Stock
    participant Notif as Notifications

    Chef->>App: crée une recette (brouillon)
    App->>Recette: enregistre (statut BROUILLON)
    Chef->>App: propose la recette
    App->>Recette: statut := A_VALIDER
    App->>Notif: notifie l'intendant (RECETTE_A_VALIDER)

    Intendant->>App: ouvre la recette à valider
    App->>Recette: coût, allergènes, nutrition
    App->>Stock: disponibilité de chaque ingrédient
    Stock-->>App: suffisant / insuffisant par ingrédient
    App-->>Intendant: fiche complète + ingrédients manquants

    alt Tous les ingrédients disponibles
        Intendant->>App: valide
        App->>Recette: statut := VALIDEE
        App-->>Chef: notification « recette validée »
        Note over Recette: Utilisable dans un menu (S-10)
    else Un ingrédient manque
        Intendant->>App: refuse + motif
        App->>Recette: statut := REFUSEE
        App->>Notif: notifie le chef (STOCK_INSUFFISANT)
        App-->>Chef: motif du refus
    end
```
