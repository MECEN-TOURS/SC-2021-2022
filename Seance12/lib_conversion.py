"""Description.

Encode une fonction permettant de passer d'un objet de type Probleme aux tableaux numpy attendus par scipy.optimize.linprog
"""
import numpy as np
from typing import Any
from dataclasses import dataclass
from lib_probleme import Probleme

@dataclass
class Tableaux:
    l: np.ndarray
    u: np.ndarray
    Aeq: np.ndarray
    beq: np.ndarray
    c: np.ndarray
    
    def __post_init__(self):
        if self.l.shape != self.u.shape or self.l.shape != self.c.shape:
            raise ValueError("Incompatibilité de dimensions pour l,u ou c.")
        if self.Aeq.ndim != 2:
            raise ValueError("Aeq doit être de dimension 2.")
        lignes, colonnes = self.Aeq.shape
        if self.l.shape != (colonnes,):
            raise ValueError("Aeq n'a pas le bon nombre de colonnes par rapport à l, u et c.")
        if self.beq.shape != (lignes,):
            raise ValueError("Aeq n'a pas le bon nombre de lignes par rapport à beq.")
            
    def __eq__(self, autre: Any):
        if type(self) != type(autre):
            return False
        if (self.l != autre.l).any():
            return False
        if (self.u != autre.u).any():
            return False
        if (self.Aeq != autre.Aeq).any():
            return False
        if (self.beq != autre.beq).any():
            return False
        if (self.c != autre.c).any():
            return False 
        return True
        
        
def decision_matrice(depart, arrivee, courant):
        if depart == courant:
            return -1
        if arrivee == courant:
            return 1
        return 0

def convertit(probleme: Probleme) -> Tableaux:
    return Tableaux(
        l = np.array([0 for _ in probleme.arretes()]),
        u = np.array([capacite for (_,_, capacite) in probleme.arretes()]),
        c = np.array(
            [
                -1 if depart == probleme._source else 0 
                for (depart,_, capacite) in probleme.arretes()
            ]
        ),
        beq = np.array(
            [
                0 for sommet in probleme.sommets_internes()
            ]
        ),
        
        Aeq = np.array(
            [
                [
                    decision_matrice(depart, arrivee, sommet)
                    for depart, arrivee, capacite in probleme.arretes()
                ]
                for sommet in probleme.sommets_internes()
            ]
        ),
    )