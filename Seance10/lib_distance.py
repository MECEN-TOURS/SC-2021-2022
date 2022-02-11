"""Description.

Librairie permettant de résoudre des problèmes de distance minimale entre point d'un graphe.
"""

from lib_graphe import Graphe

def _calcule_suivante(graphe: Graphe, depart: str, distance: dict[str, float]) -> dict[str, float]:
    resultat = dict()
    for sommet in graphe.sommets():
        resultat[sommet] = min(
            poids + distance[predecesseur] for predecesseur, poids in graphe[sommet]
        )
    resultat[depart] = 0.0
    return resultat

def calcule_distance(graphe: Graphe, depart: str, arrivee: str) -> float:
    d0 = {sommet: float("inf") for sommet in graphe.sommets()}
    d0[depart] = 0.0
    d1 = _calcule_suivante(graphe, depart, d0)
    while d1 != d0:
        d0, d1 = d1, _calcule_suivante(graphe, depart, d1)
    return d1[arrivee]