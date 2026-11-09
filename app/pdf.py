from html import escape
from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


def _texte_type(type_plat) -> str:
    return str(getattr(type_plat, "value", type_plat))


def _paragraph(texte: str, style) -> Paragraph:
    return Paragraph(escape(str(texte)).replace("\n", "<br/>"), style)


def pdf_recette(recette, cout: float, allergenes: list[str], nutrition: dict[str, float]) -> bytes:
    styles = getSampleStyleSheet()
    titre = ParagraphStyle(
        "TitreRecette",
        parent=styles["Title"],
        alignment=TA_CENTER,
        spaceAfter=8 * mm,
    )
    sous_titre = ParagraphStyle("SousTitreRecette", parent=styles["Normal"], alignment=TA_CENTER)
    normal = styles["BodyText"]
    elements = [
        _paragraph(recette.titre, titre),
        _paragraph(
            f"Type : {_texte_type(recette.type)}"
            + (" — recette végétarienne" if recette.vegetarien else ""),
            sous_titre,
        ),
        Spacer(1, 6 * mm),
    ]

    ingredients = [["Ingrédient", "Quantité (g)"]]
    ingredients.extend(
        [_paragraph(ligne.ingredient.nom, normal), f"{ligne.quantite:g}"]
        for ligne in recette.lignes
    )
    tableau = Table(ingredients, colWidths=[110 * mm, 35 * mm], repeatRows=1)
    tableau.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eeeeee")),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ALIGN", (1, 1), (1, -1), "RIGHT"),
            ]
        )
    )
    elements.extend([tableau, Spacer(1, 5 * mm)])

    elements.extend(
        [
            _paragraph(f"Coût total : {cout:.2f} €", normal),
            _paragraph(
                "Allergènes : " + (", ".join(map(str, allergenes)) if allergenes else "aucun"),
                normal,
            ),
            _paragraph(
                "Nutrition pour 100 g : "
                + ", ".join(f"{nom} : {valeur:g}" for nom, valeur in nutrition.items()),
                normal,
            ),
            Spacer(1, 5 * mm),
            _paragraph("Procédure", styles["Heading2"]),
            _paragraph(recette.procedure, normal),
        ]
    )

    sortie = BytesIO()
    document = SimpleDocTemplate(
        sortie,
        pagesize=A4,
        rightMargin=20 * mm,
        leftMargin=20 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title=recette.titre,
    )
    document.build(elements)
    return sortie.getvalue()
