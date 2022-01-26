"""Description.

Librairie pour manipuler des arbres et du code xml.
"""

from dataclasses import dataclass
from typing import Any, Union

@dataclass
class Feuille:
    nom: str
    
    def __str__(self) -> str:
        return f"<{self.nom}></{self.nom}>"
    
class Assemblage:
    def __init__(self, nom: str, sous_arbres: list["Arbre"]):
        self.nom = nom
        self.sous_arbres = sous_arbres
        
    def __repr__(self) -> str:
        return f"Assemblage(nom={repr(self.nom)}, sous_arbres={repr(self.sous_arbres)})"
        
    def __str__(self) -> str:
        str_sous_arbres = "".join([str(sous_arbre) for sous_arbre in self.sous_arbres])
        return f"<{self.nom}>{str_sous_arbres}</{self.nom}>"
    
    def __eq__(self, autre: Any) -> bool:
        if type(self) != type(autre):
            return False
        #return str(self) == str(autre)
        if self.nom != autre.nom:
            return False
        return all(gauche == droite for gauche, droite in zip(self.sous_arbres, autre.sous_arbres))
        
Arbre = Union[Feuille, Assemblage]

f = Feuille(nom="a")

def _supprime_blancs(message: str) -> str:
    return message.replace(" ", "").replace("\t", "").replace("\n", "")

def _identifie_premiere_balise(code: str) -> str:
    indice_chevron = code.find(">")
    if indice_chevron == -1:
        raise ValueError("Pas de chevron fermant!")
    resultat = code[1:indice_chevron]
    if f"<{resultat}>" == code[:1+indice_chevron]:
        return resultat
    raise ValueError("Pas une balise valide.")

def parser(code: str) -> Arbre:
    ...


    
