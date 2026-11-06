# Rôles et responsabilités (T-03)

Équipe de 4 personnes simulant une petite équipe de développement. Les rôles Scrum sont
cumulés avec le développement : chacun code, en plus de sa responsabilité transverse.

## Rôles Scrum

| Rôle | Qui | Responsabilités |
| --- | --- | --- |
| **Product Owner** | l'enseignant | Porte les besoins, priorise le backlog, valide les démos, peut faire évoluer ses exigences à chaque sprint |
| **Scrum Master** | Younes Ben Dhiab | Anime les rituels, veille au respect du process et de la DoD, lève les blocages, tient le board à jour |
| **Équipe de développement** | les 4 membres | Estime, s'engage sur le contenu du sprint, développe, teste, livre |

## Responsabilités transverses

Chaque membre porte un domaine, sans en être l'unique exécutant : il garantit que le sujet
avance et n'est pas oublié en fin de sprint.

| Membre | Responsabilité transverse | Contenu |
| --- | --- | --- |
| Adam Youssef--Muzzi | Documentation et modélisation | UML, rapport final, cohérence de `docs/` |
| Younes Ben Dhiab | Process et qualité (Scrum Master) | DoD, relecture et approbation des PR, rétrospectives |
| Aziz Mdallel | Outils de suivi | Board Notion, exports backlog, accès PO |
| Youssef Essid | Tests | Stratégie de test, rapports de tests par sprint |

> **Note :** Younes Ben Dhiab cumule le rôle de Scrum Master et le développement. Le rôle peut
> être tourné à chaque sprint si l'équipe le souhaite — dans ce cas, le noter dans la page de
> sprint concernée. Chaque membre développe, en plus de sa responsabilité transverse.

## Règles de fonctionnement

- **Décisions techniques** : discussion en équipe ; si pas de consensus, on tranche à la
  majorité et on écrit un ADR dans `docs/adr/`.
- **Décisions fonctionnelles** : elles appartiennent au PO. En cas de doute sur un besoin, on
  pose la question en réunion plutôt que de supposer, et la réponse va dans le CR.
- **Interlocuteur du PO** : une seule personne porte la parole en démo (de préférence le Scrum
  Master), pour éviter les messages contradictoires. Tout le monde peut répondre aux questions.
- **Communication technique adaptée** : le PO n'est pas nécessairement technique — on démontre
  des comportements du produit, pas des bouts de code.
- **Absence** : la personne absente prévient l'équipe et ses tâches sont réaffectées en début
  de séance ; la réaffectation est notée dans la page de sprint.
