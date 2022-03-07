"""Description.

Librairie de gestion des graphes.

Générique autour du type S représentant un sommet.
Expose la fonction calcule_chemin et l'exception PasDeChemin.
"""
from typing import TypeVar

S = TypeVar("S")


class PasDeChemin(Exception):
    pass


def _calcule_voisins(depart: S, arretes: list[tuple[S, S]]) -> list[S]:
    """Renvoie la liste des sommets accessibles en un pas depuis depart.
    Exemples:
    >>> _calcule_voisins(depart=1, arretes=[(1, 2), (1, 3)])
    [2, 3]
    >>> _calcule_voisins(depart=1, arretes=[(1, 1), (1, 2), (1, 3)])
    [2, 3]"""
    return [e2 for (e1, e2) in arretes if e1 == depart and e2 != depart]


def _elague_sommets(a_enlever: S, sommets: list[S]) -> list[S]:
    """Enleve le sommet de la liste.
    Exemples:
    >>> _elague_sommets(a_enlever=1, sommets=[1, 2, 3])
    [2, 3]
    >>> _elague_sommets(a_enlever=4, sommets=[1, 2, 3])
    [1, 2, 3]"""
    return [etat for etat in sommets if a_enlever != etat]


def _elague_arretes(a_enlever: S, arretes: list[tuple[S, S]]) -> list[tuple[S, S]]:
    """Enleve les références à a_enlever de la liste des arrêtes.
    Exemples
    >>> _elague_arretes(a_enlever=1, arretes=[(1, 1), (1, 2), (1, 3)])
    []
    >>> _elague_arretes(a_enlever=1, arretes=[(1, 1), (1, 2), (1, 3), (2, 3)])
    [(2, 3)]"""

    return [(e1, e2) for (e1, e2) in arretes if e1 != a_enlever and e2 != a_enlever]


def calcule_chemin(
    depart: S, arrivee: S, sommets: list[S], arretes: list[tuple[S, S]]
) -> list[S]:
    """Détermine un chemin de depart à arrivee dans le graphe.
    Si un tel chemin n'existe pas l'exception PasDeChemin est soulevée.
    On trouve toujours un chemin sans boucle.
    Exemples:
    >>> calcule_chemin(
    ...         depart=1,
    ...         arrivee=4,
    ...         sommets=[1, 2, 3, 4],
    ...         arretes=[(1, 1), (1, 2), (1, 3), (2, 4)]
    ...     )
    [1, 2, 4]
    >>> calcule_chemin(
    ...             depart=4,
    ...             arrivee=1,
    ...             sommets=[1, 2, 3, 4],
    ...             arretes=[(1, 1), (1, 2), (1, 3), (2, 4)]
    ...         )
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "C:\\Users\\perrollaz\\Documents\\graphe.py", line 51, in calcule_chemin
    __main__.PasDeChemin
    """
    if depart == arrivee:
        return [depart]
    sommets_elagues = _elague_sommets(a_enlever=depart, sommets=sommets)
    arretes_elaguees = _elague_arretes(a_enlever=depart, arretes=arretes)
    for voisin in _calcule_voisins(depart, arretes):
        try:
            resultat_intermediaire = calcule_chemin(
                depart=voisin,
                arrivee=arrivee,
                sommets=sommets_elagues,
                arretes=arretes_elaguees,
            )
        except PasDeChemin:
            pass
        else:
            return [depart] + resultat_intermediaire

    raise PasDeChemin
