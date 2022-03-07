"""Description.

Fonctionnalités de conversion du problème brute vers un graphe.
"""
from .data import Donnees
from enum import Enum
from itertools import product

class Cote(Enum):
    GAUCHE = "rive gauche"
    DROIT = "rive droite"

Etat = dict[str, Cote]

def _verifie_contrainte(etat: Etat, contrainte: tuple[str, list[str]]) -> bool:
    superviseur, supervises = contrainte
    cotes = {etat[supervise] for supervise in supervises}
    if len(cotes) != 1:
        return True
    return etat[superviseur] in cotes

def _genere_etats(donnees: Donnees) -> list[Etat]:
    resultat = list()
    for choix in product(*[(Cote.GAUCHE, Cote.DROIT) for _ in donnees.personnages]):
        resultat.append(
            {
                personnages: cote
                for personnages, cote in zip(donnees.personnages, choix)
            }
        )
    return resultat

def _genere_sommets(donnees) -> list[Etat]:
    etats = _genere_etats(donnees)
    return [
        etat for etat in etats if all(_verifie_contrainte(etat=etat, contrainte=contrainte) for contrainte in donnees.contraintes)
    ]

def _sont_relies(depart: Etat, arrivee: Etat, donnees: Donnees) -> bool:
    changent_de_cotes = [personnage for personnage in donnees.personnages if depart[personnage] != arrivee[personnage]]
    if len(changent_de_cotes) > donnees.nb_places:
        return False
    cotes_fin = {arrivee[personnage] for personnage in changent_de_cotes}
    if len(cotes_fin) != 1:
        return False
    for personnage in changent_de_cotes:
        if personnage in donnees.rameurs:
            return True
    return False

def convertit(donnees: Donnees) -> tuple[list[Etat], list[tuple[Etat, Etat]]]:
    sommets = _genere_sommets(donnees)
    arretes = [
        (depart, arrivee) for depart in sommets for arrivee in sommets if _sont_relies(depart=depart, arrivee=arrivee, donnees=donnees)
    ]
    
    return sommets, arretes