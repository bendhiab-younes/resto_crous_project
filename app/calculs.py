"""Calculs dérivés d'une recette, à partir de ses lignes (quantités en grammes)."""

NUTRIMENTS = ("calories", "proteines", "glucides", "lipides")


def cout_recette(lignes) -> float:
    return sum((ligne.quantite / 1000 * ligne.ingredient.cout_par_kg for ligne in lignes), 0.0)


def nutrition_pour_100g(lignes) -> dict[str, float]:
    quantite_totale = sum(ligne.quantite for ligne in lignes)
    if quantite_totale == 0:
        raise ValueError("La quantité totale de la recette est nulle.")
    return {
        nutriment: sum(ligne.quantite * getattr(ligne.ingredient, nutriment) for ligne in lignes)
        / quantite_totale
        for nutriment in NUTRIMENTS
    }


def allergenes_recette(lignes) -> list[str]:
    return sorted({allergene.nom for ligne in lignes for allergene in ligne.ingredient.allergenes})


def ingredients_manquants(lignes, stocks: dict[int, float]) -> list[str]:
    besoins: dict[int, float] = {}
    noms: dict[int, str] = {}
    for ligne in lignes:
        besoins[ligne.ingredient.id] = besoins.get(ligne.ingredient.id, 0.0) + ligne.quantite
        noms[ligne.ingredient.id] = ligne.ingredient.nom
    return sorted(
        noms[identifiant]
        for identifiant, besoin in besoins.items()
        if besoin > stocks.get(identifiant, 0.0)
    )
