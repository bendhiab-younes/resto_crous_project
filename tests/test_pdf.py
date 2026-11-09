import re
from types import SimpleNamespace

from app.pdf import pdf_recette


def recette(procedure="Mélanger les ingrédients."):
    return SimpleNamespace(
        titre="Soupe de légumes",
        type="LEGUME",
        vegetarien=True,
        procedure=procedure,
        lignes=[
            SimpleNamespace(
                quantite=250,
                ingredient=SimpleNamespace(nom="Carotte"),
            )
        ],
    )


def test_TC_S17_01_pdf_recette_genere_un_document_pdf():
    resultat = pdf_recette(
        recette(),
        cout=2.5,
        allergenes=["Céleri"],
        nutrition={"calories": 42, "proteines": 1.2},
    )

    assert resultat.startswith(b"%PDF")


def test_TC_S17_02_pdf_sans_allergene_et_procedure_longue():
    procedure = "Étape détaillée. " * 2000

    resultat = pdf_recette(
        recette(procedure),
        cout=0,
        allergenes=[],
        nutrition={"calories": 0},
    )

    assert resultat.startswith(b"%PDF")
    assert re.search(rb"/Count [2-9]", resultat)
