"""Description.

Donnée du problème.
"""

from serde import serde

@serde
class Donnees:
    personnages: list[str]
    nb_places: int
    rameurs: list[str]
    contraintes: list[tuple[str, list[str]]]
    
    def __post_init__(self):
        if self.nb_places <= 0:
            raise ValueError("Il doit y avoir un nombre de places positif.")
        for rameur in self.rameurs:
            if rameur not in  self.personnages:
                raise ValueError("Les rameurs doivent être des personnages déclarés.")
        for superviseur, supervises in self.contraintes:
            if superviseur not in self.personnages:
                raise ValueError("Les superviseurs doivent être des personnages déclarés.")
            for supervise in supervises:
                if supervise not in self.personnages:
                    raise ValueError("Les supervisés doivent être des personnages déclarés.")
                