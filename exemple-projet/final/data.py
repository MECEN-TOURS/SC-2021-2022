"""Description.

Classe Permettant de représenter les données d'un problème.
"""

from serde import serde


@serde
class Donnees:
    """Représente les données d'un problème de traversée.

    personnages: liste des caractères
    nb_places: nombre de places disponible dans la barque pour effectuer une traversée
    rameurs: liste des personnages sachant ramer
    contraintes: liste de couples superviseur (personnage) / supervisés (liste de personnages)

    On vérifie après l'instanciation que le problème est "raisonnable":
     - nombres de personnes dans la barque positif,
     - rameurs, superviseurs et supervisés sont bien des personnages.

    La sérialisation est fait automatiquement vers json, yaml et toml via pyserde.

    Exemple:
    >>> essai = Donnees(
    ...     personnages=["Berger", "Loup", "Mouton", "Choux"],
    ...     nb_places=2,
    ...     rameurs=["Berger"],
    ...     contraintes=[
    ...         ("Berger", ["Loup", "Mouton"]),
    ...         ("Berger", ["Mouton", "Choux"]),
    ...     ],
    ... )
    >>> essai
    Donnees(personnages=['Berger', 'Loup', 'Mouton', 'Choux'], nb_places=2, rameurs=['Berger'],
    contraintes=[('Berger', ['Loup', 'Mouton']), ('Berger', ['Mouton', 'Choux'])])
    >>> from serde.json import to_json, from_json
    >>> code = to_json(essai)
    >>> code
    '{"personnages": ["Berger", "Loup", "Mouton", "Choux"], "nb_places": 2, "rameurs": ["Berger"],
    "contraintes": [["Berger", ["Loup", "Mouton"]], ["Berger", ["Mouton", "Choux"]]]}'
    >>> decode = from_json(Donnees, code)
    >>> decode
    Donnees(personnages=['Berger', 'Loup', 'Mouton', 'Choux'], nb_places=2, rameurs=['Berger'],
    contraintes=[('Berger', ['Loup', 'Mouton']), ('Berger', ['Mouton', 'Choux'])])
    """

    personnages: list[str]
    nb_places: int
    rameurs: list[str]
    contraintes: list[tuple[str, list[str]]]

    def __post_init__(self):
        if self.nb_places <= 0:
            raise ValueError("Il doit y avoir un nombre de places positif.")
        for rameur in self.rameurs:
            if rameur not in self.personnages:
                raise ValueError("Les rameurs doivent être des personnages déclarés.")
        for superviseur, supervises in self.contraintes:
            if superviseur not in self.personnages:
                raise ValueError(
                    "Les superviseurs doivent être des personnages déclarés."
                )
            for supervise in supervises:
                if supervise not in self.personnages:
                    raise ValueError(
                        "Les supervisés doivent être des personnages déclarés."
                    )
