"""Description.

Librairie permettant de construire le graphe associé au problème de rivière.
"""


from enum import Enum
from dataclasses import dataclass

class Rive(Enum):
    GAUCHE = "gauche"
    DROITE = "droite"
    
@dataclass
class Etat:
    berger: Rive
    loup: Rive
    mouton: Rive
    chou: Rive
    

def est_valide(etat: Etat) -> bool:
    """Vérifie si la règle de supervision est respectée.
    """
    if etat.berger != etat.loup and etat.loup == etat.mouton:
        return False
    if etat.berger != etat.chou and etat.chou == etat.mouton:
        return False
    return True


def sont_connectes(depart: Etat, arrivee: Etat) -> bool:
    if depart.berger == arrivee.berger:
        return False
    
    nombre_changements = 0
    if depart.loup != arrivee.loup:
        nombre_changements += 1
    if depart.mouton != arrivee.mouton:
        nombre_changements += 1
    if depart.chou != arrivee.chou:
        nombre_changements += 1
        
    if nombre_changements <= 1:
        return True
    else:
        return False
    
def genere_message(depart: Etat, arrivee: Etat) -> str:
    if depart.loup != arrivee.loup:
        return f"Berger, Loup  : {depart.loup} -> {arrivee.loup}"
    if depart.mouton != arrivee.mouton:
        return f"Berger, Mouton: {depart.mouton} -> {arrivee.mouton}"
    if depart.chou != arrivee.chou:
        return f"Berger, Chou  : {depart.chou} -> {arrivee.chou}"
    return     f"Berger        : {depart.berger} -> {arrivee.berger}"

def visualise_chemin(etats: list[Etat]) -> str:
    resultat = list()
    for e1, e2 in zip(etats[:-1], etats[1:]):
        if not sont_connectes(e1, e2):
            return "Ce n'est pas un chemin."
        resultat.append(genere_message(depart=e1, arrivee=e2))
    return "\n".join(resultat)
    
Arrete = tuple[Etat, Etat]

DEPART = Etat(
    berger=Rive.DROITE, 
    mouton=Rive.DROITE, 
    loup=Rive.DROITE, 
    chou=Rive.DROITE
)

ARRIVEE = Etat(
    berger=Rive.GAUCHE, 
    mouton=Rive.GAUCHE, 
    loup=Rive.GAUCHE, 
    chou=Rive.GAUCHE
)

ETATS: list[Etat] = [
    Etat(
        berger=choix_berger,
        loup=choix_loup,
        mouton=choix_mouton,
        chou = choix_chou,
    )
    for choix_berger in Rive
    for choix_loup in Rive
    for choix_mouton in Rive
    for choix_chou in Rive
]

SOMMETS: list[Etat] = [etat for etat  in ETATS if est_valide(etat)]

ARRETES: list[Arrete] = [
    (e1, e2) 
    for e1 in SOMMETS 
    for e2 in SOMMETS 
    if sont_connectes(depart=e1, arrivee=e2)
]