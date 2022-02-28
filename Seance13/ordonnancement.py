"""Description.

Fonctionnalités pour le problème d'ordonnancement.
"""
from typing import Generator, Union
from rich.table import Table


def _cherche_sans_prerequis(cahier_des_charges: dict[str, list[str]]) -> list[str]:
    return [tache for tache, prerequiss in cahier_des_charges.items() if prerequiss == []]

def _elague_cdc(cahier_des_charges: dict[str, list[str]], a_effectuer: str) -> dict[str, list[str]]:
    return {
        tache: [prerequis for prerequis in prerequiss if prerequis != a_effectuer]
        for tache, prerequiss in cahier_des_charges.items()
        if tache != a_effectuer
    }

def ordonnance(cahier_des_charges: dict[str, list[str]]) -> list[str]:
    a_choisir = _cherche_sans_prerequis(cahier_des_charges)
    if a_choisir == []:
        if cahier_des_charges == {}:
            return []
        else:
            raise ValueError("Il n'y a pas d'ordonnancement possible")
    a_effectuer, *_ = a_choisir
    nouveau = _elague_cdc(cahier_des_charges=cahier_des_charges, a_effectuer=a_effectuer)
    resultat = [a_effectuer]
    resultat.extend(ordonnance(nouveau))
    return resultat

def genere_ordres(cahier_des_charges: dict[str, list[str]]) -> Generator[list[str], None, None]:
    a_choisir = _cherche_sans_prerequis(cahier_des_charges)
    if a_choisir == []:
        if cahier_des_charges == {}:
            yield []
        else:
            raise ValueError("Il n'y a pas d'ordonnancement possible")
    for a_effectuer in a_choisir:
        nouveau = _elague_cdc(cahier_des_charges=cahier_des_charges, a_effectuer=a_effectuer)
        
        for ordre_suite in genere_ordres(nouveau):
            resultat = [a_effectuer]
            resultat.extend(ordre_suite)
            yield resultat
            
            
def edt_parallele(
    cdc: dict[str, tuple[list[str], Union[float, int]]]
) -> dict[str, tuple[Union[float, int], Union[float, int]]]:
    ordre = ordonnance(
        {
            tache: prerequis
            for tache, (prerequis, _) in cdc.items()
        }
    )
    resultat = dict()
    for tache in ordre:
        prerequis, duree = cdc[tache]
        if prerequis == []:
            debut = 0
        else:
            debut = max(resultat[precedent][1] for precedent in prerequis)
        resultat[tache] = (debut, debut + duree)
    return resultat

def cdc_to_table(cdc: dict[str, tuple[list[str], Union[float, int]]]) -> Table:
    resultat = Table("Tâche", "Prérequis", "Durée")
    for (tache, (prerequis, duree)) in cdc.items():
        resultat.add_row(
            str(tache), 
            " ".join([str(precedent) for precedent in prerequis]), 
            str(duree)
        )
    return resultat