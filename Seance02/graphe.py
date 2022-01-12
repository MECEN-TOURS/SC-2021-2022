"""Description.

Librairie contenant une fonction permettant de calculer des chemins dans un graphe.
"""

from typing import TypeVar

S = TypeVar("S")
A = tuple[S, S]

class PasDeChemin(Exception):
    pass

def calcule_voisins(depart: S, arretes: list[A]) -> list[S]:
    return [e2 for (e1, e2) in arretes if e1 == depart and e2 != depart]

def elague_sommets(a_enlever: S, sommets: list[S]) -> list[S]:
    return [etat for etat in sommets if a_enlever != etat]

def elague_arretes(a_enlever: S, arretes: list[A]) -> list[A]:
    return [
        (e1, e2) 
        for (e1, e2) in arretes 
        if e1 != a_enlever and e2 != a_enlever
    ]

def calcule_chemin(
    depart: S, 
    arrivee: S, 
    sommets: list[S], 
    arretes: list[A]
) -> list[S]:
    if depart == arrivee:
        return [depart]
    sommets_elagues = elague_sommets(a_enlever=depart, sommets=sommets)
    arretes_elaguees = elague_arretes(a_enlever=depart, arretes=arretes)
    for voisin in calcule_voisins(depart, arretes):
        try:
            resultat_intermediaire = calcule_chemin(
                depart=voisin,
                arrivee=arrivee,
                sommets=sommets_elagues,
                arretes=arretes_elaguees
            )
        except PasDeChemin:
            pass
        else:
            return [depart] + resultat_intermediaire
            
    raise PasDeChemin