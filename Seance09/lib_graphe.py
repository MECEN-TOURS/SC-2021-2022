"""Description.

Librairie représentant un objet graphe avec une fonctionnalité permettant d'exporter en .dot
"""
from typing import Any


class Graphe:
    def __init__(self, sommets: list[str], arretes: list[tuple[str, str]]):
        self._sommets = sommets
        self._arretes = arretes
        
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

        
def genere_dot(graphe: Graphe) -> str:
    lignes = [f"{depart} -> {arrivee};" for depart, arrivee in graphe]
    interne = "\n".join(lignes)
    return f"""
digraph {{
{interne}
}}
"""
def _gere_ligne(ligne: str) -> tuple[str, str]:
    indice_coupure = ligne.find(" -> ")
    depart = ligne[:indice_coupure]
    arrivee = ligne[indice_coupure + 4: -1]
    return depart, arrivee

def genere_graphe(code_dot: str) -> Graphe:
    lignes = code_dot.strip()[1:-1]
    arretes = set()
    sommets = set()
    for ligne in lignes:
        depart, arrivee = _gere_ligne(ligne)
        arretes.add((depart, arrivee))
        sommets.add(depart)
        sommets.add(arrivee) 
    # à inspecter
    return Graphe(sommets=list(sommets), arretes=list(arretes))