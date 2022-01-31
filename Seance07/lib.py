"""Description.

Librairie pour manipuler des arbres et du code xml.

TODO:
    - spliter _decoupe_code
    - rajouter des tests pour _decoupe_code 
    - vérifier les cas limites par rapport à la signature
"""

from dataclasses import dataclass
from typing import Any, Optional


class Arbre:
    def __init__(self, nom: str, sous_arbres: Optional[list["Arbre"]] = None):
        self.nom = nom
        if sous_arbres is None:
            self.sous_arbres = []
        else:
            self.sous_arbres = sous_arbres

    def __repr__(self) -> str:
        if self.sous_arbres == []:
            return f"Arbre(nom={repr(self.nom)})"
        return f"Arbre(nom={repr(self.nom)}, sous_arbres={repr(self.sous_arbres)})"

    def __str__(self) -> str:
        str_sous_arbres = "".join([str(sous_arbre) for sous_arbre in self.sous_arbres])
        return f"<{self.nom}>{str_sous_arbres}</{self.nom}>"

    def __eq__(self, autre: Any) -> bool:
        if type(self) != type(autre):
            return False
        # return str(self) == str(autre)
        if self.nom != autre.nom:
            return False
        return all(
            gauche == droite
            for gauche, droite in zip(self.sous_arbres, autre.sous_arbres)
        )


def _supprime_blancs(message: str) -> str:
    return message.replace(" ", "").replace("\t", "").replace("\n", "")


def _identifie_premiere_balise(code: str) -> str:
    indice_chevron = code.find(">")
    if indice_chevron == -1:
        raise ValueError("Pas de chevron fermant!")
    resultat = code[1:indice_chevron]
    if f"<{resultat}>" == code[: 1 + indice_chevron]:
        return resultat
    raise ValueError("Pas une balise valide.")


def _identifie_indice_balise_fermante(balise: str, code: str) -> int:
    indice = code.find(f"</{balise}>")
    if indice != -1:
        return indice
    raise ValueError("La balise fermante n'existe pas dans le code.")


def _extrait_interieur(code: str) -> str:
    premiere_balise = _identifie_premiere_balise(code)
    indice_ouvrant = len(premiere_balise) + 2
    indice_fermant = _identifie_indice_balise_fermante(
        balise=premiere_balise, code=code
    )
    return code[indice_ouvrant:indice_fermant]


def _decoupe_code(code: str) -> list[str]:
    if code == "":
        return []
    premiere_balise = _identifie_premiere_balise(code)
    indice_fermant = _identifie_indice_balise_fermante(
        balise=premiere_balise, code=code
    )
    indice_coupure = indice_fermant + 3 + len(premiere_balise)
    gauche, droite = code[:indice_coupure], code[indice_coupure:]
    resultat = [gauche]
    resultat.extend(_decoupe_code(droite))
    return resultat


def parser(code: str) -> Arbre:
    nettoye = _supprime_blancs(code)
    premiere_balise = _identifie_premiere_balise(nettoye)
    interieur = _extrait_interieur(nettoye)
    sous_codes = _decoupe_code(interieur)
    return Arbre(
        nom=premiere_balise, sous_arbres=[parser(sous_code) for sous_code in sous_codes]
    )
