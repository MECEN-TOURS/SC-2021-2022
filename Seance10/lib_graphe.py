"""Description.

Librairie représentant un objet graphe avec une fonctionnalité permettant d'exporter en .dot
"""
from typing import Any, Union


class Graphe:
    def __init__(
        self, sommets: list[str], arretes: list[tuple[str, str, Union[int, float]]]
    ):
        self._sommets = sommets
        self._arretes: list[tuple[str, str, float]] = [
            (depart, arrivee, float(poids)) for depart, arrivee, poids in arretes
        ]

    def __repr__(self) -> str:
        return f"Graphe(sommets={repr(self._sommets)}, arretes={repr(self._arretes)})"

    def __eq__(self, autre: Any) -> bool:
        if type(autre) != type(self):
            return False
        if sorted(self._sommets) != sorted(autre._sommets):
            return False
        if sorted(self._arretes) != sorted(autre._arretes):
            return False
        return True

    def __iter__(self):
        return iter(self._arretes)
    
    def sommets(self):
        return iter(self._sommets)
    
    def __getitem__(self, arrivee: str):
        for gauche, droite, poids in self:
            if droite == arrivee:
                yield gauche, poids


def genere_dot(graphe: Graphe) -> str:
    lignes = [f"{depart} -> {arrivee} [label={poids}];" for depart, arrivee, poids in graphe]
    interne = "\n".join(lignes)
    return f"""
digraph {{
{interne}
}}
"""


def _gere_ligne(ligne: str) -> tuple[str, str, float]:
    indice_coupure = ligne.find(" -> ")
    depart = ligne[:indice_coupure]
    reste = ligne[indice_coupure + 4 : -1]
    indice_espace = reste.find(" [label=")
    arrivee = reste[:indice_espace]
    poids = float(reste[indice_espace+8:-1])
    return depart, arrivee, poids


def _decoupe_interieur(code: str) -> list[str]:
    return code.strip().splitlines()[1:-1]


def genere_graphe(code_dot: str) -> Graphe:
    lignes = _decoupe_interieur(code=code_dot)
    arretes = set()
    sommets = set()
    for ligne in lignes:
        depart, arrivee, poids = _gere_ligne(ligne)
        arretes.add((depart, arrivee, poids))
        sommets.add(depart)
        sommets.add(arrivee)
    return Graphe(sommets=list(sommets), arretes=list(arretes))
