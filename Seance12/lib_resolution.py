"""Description.

Module contenant les fonctionnalités de résolution d'un problème de flot maximal.
"""
from lib_probleme import Probleme
from lib_conversion import Tableaux, convertit
from typing import Any, Union
from scipy.optimize import linprog

class Solution:
    def __init__(
        self, 
        sommets: list[str], 
        arretes: list[tuple[str, str, Union[float, int]]], 
        source: str, 
        puit: str
    ):
        self._sommets = sommets
        self._arretes: list[tuple[str, str, float]] = [
            (depart, arrivee, float(flot)) for depart, arrivee, flot in arretes
        ]
        if source not in sommets:
            raise ValueError("La source doit être un sommet.")
        self._source = source
        if puit not in sommets:
            raise ValueError("Le puit doit être un sommet.")
        self._puit = puit
        
    def __repr__(self) -> str:
        return f"Solution(sommets={repr(self._sommets)}, arretes={repr(self._arretes)}, source={repr(self._source)}, puit={repr(self._puit)})"
        
    def __eq__(self, autre: Any) -> bool:
        if type(self) != type(autre):
            return False
        if self._source != autre._source:
            return False
        if self._puit != autre._puit:
            return False
        if sorted(self._sommets) != sorted(autre._sommets):
            return False
        if sorted(self._arretes) != sorted(autre._arretes):
            return False
        return True


def resout(probleme: Probleme) -> Solution:
    donnees_numeriques = convertit(probleme)
    resultat_numerique = linprog(
        c=donnees_numeriques.c,
        A_eq=donnees_numeriques.Aeq,
        b_eq=donnees_numeriques.beq,
        bounds=[(l, u) for l,u in zip(donnees_numeriques.l, donnees_numeriques.u)],
        method="simplex",
    )
    if not resultat_numerique.success:
        raise ValueError("Pas de solution?")
    return Solution(
        sommets=list(probleme.sommets()),
        arretes=[
            (depart, arrivee, flot) 
            for ((depart, arrivee, _), flot) in zip(probleme.arretes(), resultat_numerique.x)
        ],
        source=probleme.source(),
        puit=probleme.puit(),
    )
    