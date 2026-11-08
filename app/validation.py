import math


def lire_nombre(valeur: str) -> float | None:
    """Convertit une saisie (virgule décimale acceptée), `None` si ce n'est pas un nombre fini."""
    try:
        nombre = float(valeur.strip().replace(",", "."))
    except ValueError:
        return None
    return nombre if math.isfinite(nombre) else None
