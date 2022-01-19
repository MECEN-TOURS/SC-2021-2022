"""Description.

Librairie pour un solveur de Sudoku 4x4.
"""
from typing import Any, Optional

def _case_valide(valeur: Optional[int]) -> bool:
    if valeur is None:
        return True
    if valeur in {1, 2, 3, 4}:
        return True
    return False

class Grille:
    """
    Grille de Sudoku 4x4 partiellement remplie.
    
    On stocke les cases dans une liste 1d lignes par lignes.
    
    Une case vide contient None.
    """
    def __init__(self, cases: list[Optional[int]]):
        if len(cases) != 16:
            raise ValueError("Il doit y avoir 16 cases exactement.")
        if any(not _case_valide(case) for case in cases):
            raise ValueError("Les cases ne peuvent contenir que None 1 2 3 ou 4!")
        self._cases = cases
        
    def __str__(self) -> str:
        caracteres = [ "_" if case is None else str(case) for case in self._cases]
        return """
-----------------
| {} | {} | {} | {} |
-----------------
| {} | {} | {} | {} |
-----------------
| {} | {} | {} | {} |
-----------------
| {} | {} | {} | {} |
-----------------
""".format(*caracteres)
        
    def __repr__(self) -> str:
        return f"Grille(cases={self._cases})"
    
    def __iter__(self):
        return iter(self._cases)
    
    def __getitem__(self, indice):
        return self._cases[indice]

def _doublon_present(valeurs: list[Optional[int]]) -> bool:
    for temoin in range(1, 5):
        if sum(1 for valeur in valeurs if valeur == temoin) > 1:
            return True
    return False

def _verifie_probleme_lignes(grille: Grille) -> bool:
    for i in range(0, 4):
        if _doublon_present([grille[4 * i + j] for j in range(0, 4)]):
            return True
    return False

def _verifie_probleme_colonnes(grille: Grille) -> bool:
    for j in range(0, 4):
        if _doublon_present([grille[4 * i + j] for i in range(0, 4)]):
            return True
    return False
    
def _verifie_probleme_carres(grille: Grille) -> bool:
    for indice_carre in (0, 2, 8, 10):
        if _doublon_present(
            [
                grille[indice_carre + indice_interne] 
                for indice_interne in (0, 1, 4, 5)
            ]
        ):
            return True
    return False


def est_valide(grille: Grille) -> bool:
    if _verifie_probleme_lignes(grille):
        return False
    if _verifie_probleme_colonnes(grille):
        return False
    if _verifie_probleme_carres(grille):
        return False
    return True

def est_complete(grille: Grille) -> bool:
    ...
    
def sont_reliees(depart: Grille, arrivee: Grille) -> bool:
    ...