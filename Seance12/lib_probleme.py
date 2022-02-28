"""Description.

Module définissant une classe représentant un problème de flot maximal.

TODO: 
    - vérifier que les arrêtes sont bien avec des sommets valides
    - vérifier que les poids sont positifs 
"""
from typing import Any, Generator, Union


class Probleme:
    def __init__(
        self, 
        sommets: list[str], 
        arretes: list[tuple[str, str, Union[float, int]]], 
        source: str, 
        puit: str
    ):
        self._sommets = sommets
        self._arretes: list[tuple[str, str, float]] = [
            (depart, arrivee, float(capacite)) for depart, arrivee, capacite in arretes
        ]
        if source not in sommets:
            raise ValueError("La source doit être un sommet.")
        self._source = source
        if puit not in sommets:
            raise ValueError("Le puit doit être un sommet.")
        self._puit = puit
        
    def __repr__(self) -> str:
        return f"Probleme(sommets={repr(self._sommets)}, arretes={repr(self._arretes)}, source={repr(self._source)}, puit={repr(self._puit)})"
        
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
    
    def arretes(self) -> Generator[tuple[str, str, float], None, None]:
        return iter(self._arretes)
    
    def sommets(self) -> Generator[str, None, None]:
        return iter(self._sommets)
    
    def sommets_internes(self) -> Generator[str, None, None]:
        for sommet in self._sommets:
            if sommet != self._source and sommet != self._puit:
                yield sommet
                
    def puit(self) -> str:
        return self._puit
    
    def source(self) -> str:
        return self._source