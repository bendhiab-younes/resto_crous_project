# Modélisation UML

Les diagrammes sont écrits en **Mermaid** directement dans les fichiers Markdown :

- le source est du texte → **diffable** dans git, on voit l'évolution du modèle sprint par sprint ;
- GitHub les **rend graphiquement** sans outil ni export ;
- c'est un **format ouvert**, conforme à l'exigence du sujet ;
- les mêmes blocs peuvent être repris comme figures dans le rapport.

| Diagramme | Fichier | Tâche |
| --- | --- | --- |
| Cas d'usage | [`cas-usage.md`](cas-usage.md) | T-05 |
| Classes | [`classes.md`](classes.md) | T-06 |
| Séquence (workflow de validation) | [`sequence-validation.md`](sequence-validation.md) | complément |

> Les diagrammes sont **vivants** : à chaque sprint qui modifie le modèle, on met à jour le
> fichier dans la même PR que le code. Un diagramme qui ne correspond plus au code vaut moins
> que pas de diagramme.
