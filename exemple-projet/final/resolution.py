"""Description.

Librairie de résolution du problème complet.
"""

from .data import Donnees
from .conversion import convertit, Etat, Cote
from .graphes import calcule_chemin, PasDeChemin

def resoud(donnees: Donnees) -> list[Etat]:
    sommets, arretes = convertit(donnees)
    depart = {personnage: Cote.GAUCHE for personnage in donnees.personnages}
    arrivee = {personnage: Cote.DROIT for personnage in donnees.personnages}
    try:
        solution = calcule_chemin(
            depart=depart,
            arrivee=arrivee,
            sommets=sommets,
            arretes=arretes,
        )
    except PasDeChemin:
        raise ValueError("Le problème n'a pas de solution!")
    return solution
        
    