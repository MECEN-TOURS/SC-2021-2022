"""Description.

Librairie pour un solveur de Sudoku 4x4.

Classe:
    Grille
Fonctions:
    est_valide
    est_complete
    calcule_solutions
"""
from typing import Any, Optional, Generator


def _case_valide(valeur: Optional[int]) -> bool:
    """Vérifie si on prend les valeurs None, 1, 2, 3 ou 4.

    Exemples:
    >>> _case_valide(1)
    True
    >>> _case_valide(2)
    True
    >>> _case_valide(3)
    True
    >>> _case_valide(4)
    True
    >>> _case_valide(None)
    True
    >>> _case_valide("5")
    False
    >>> _case_valide(5)
    False
    """
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

    Exemple:
    >>> grille = Grille([1, 2, 3, 4, None, 4, 1, 2, 2, None, None, None, 4, 3, 2, 1])
    >>> repr(grille)
    'Grille(cases=[1, 2, 3, 4, None, 4, 1, 2, 2, None, None, None, 4, 3, 2, 1])'
    >>> print(grille)

    -----------------
    | 1 | 2 | 3 | 4 |
    -----------------
    | _ | 4 | 1 | 2 |
    -----------------
    | 2 | _ | _ | _ |
    -----------------
    | 4 | 3 | 2 | 1 |
    -----------------
    >> for case in grille:
    ...     print(case, end=" ")
    ...
    1 2 3 4 None 4 1 2 2 None None None 4 3 2 1
    >>> grille1 = Grille(cases=[1, 2, 3, 4, 4, 3, 2, 1, 2, 1, 4, 3, 3, 4, 1, 2])
    >>> grille2 = Grille(cases=[1, 2, 3, 4, 4, 3, 2, 1, 2, 1, 4, 3, 3, 4, 1, 2])
    >>> grille1 == grille2
    True
    >>> Grille(cases=[])
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "./Seance05/lib.py", line 52, in __init__
        raise ValueError("Il doit y avoir 16 cases exactement.")
    ValueError: Il doit y avoir 16 cases exactement.
    >>> valeurs = [None for _ in range(16)]
    >>> valeurs[5] = 5
    >>> Grille(cases=valeurs)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "./lib.py", line 54, in __init__
        raise ValueError("Les cases ne peuvent contenir que None 1 2 3 ou 4!")
    ValueError: Les cases ne peuvent contenir que None 1 2 3 ou 4!
    """

    def __init__(self, cases: list[Optional[int]]):
        if len(cases) != 16:
            raise ValueError("Il doit y avoir 16 cases exactement.")
        if any(not _case_valide(case) for case in cases):
            raise ValueError("Les cases ne peuvent contenir que None 1 2 3 ou 4!")
        self._cases = cases

    def __eq__(self, autre: Any) -> bool:
        if type(autre) != type(self):
            return False
        for case1, case2 in zip(self, autre):
            if case1 != case2:
                return False
        return True

    def __str__(self) -> str:
        caracteres = ["_" if case is None else str(case) for case in self._cases]
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
""".format(
            *caracteres
        )

    def __repr__(self) -> str:
        return f"Grille(cases={self._cases})"

    def __iter__(self):
        return iter(self._cases)

    def __getitem__(self, indice):
        return self._cases[indice]


def _doublon_present(valeurs: list[Optional[int]]) -> bool:
    """Teste si un chiffre entre 1 et 4 est répété au moins une fois.

    Exemples:
    >>> _doublon_present(valeurs=[1, 2, 3])
    False
    >>> _doublon_present(valeurs=[1, 1, 2])
    True
    >>> _doublon_present(valeurs=[None, None])
    False"""
    for temoin in range(1, 5):
        if sum(1 for valeur in valeurs if valeur == temoin) > 1:
            return True
    return False


def _verifie_probleme_lignes(grille: Grille) -> bool:
    """Vérifie si une des lignes contient une répétition.

    Exemple:
    >>> valeurs = [None for _ in range(16)]
    >>> valeurs[0], valeurs[1] = 1, 1
    >>> _verifie_probleme_lignes(grille=Grille(cases=valeurs))
    True
    """
    for i in range(0, 4):
        if _doublon_present([grille[4 * i + j] for j in range(0, 4)]):
            return True
    return False


def _verifie_probleme_colonnes(grille: Grille) -> bool:
    """Vérifie si une des colonnes contient une répétition.

    Exemple:
    >>> valeurs = [None for _ in range(16)]
    >>> valeurs[0], valeurs[4] = 1, 1
    >>> _verifie_probleme_colonnes(grille=Grille(cases=valeurs))
    True"""
    for j in range(0, 4):
        if _doublon_present([grille[4 * i + j] for i in range(0, 4)]):
            return True
    return False


def _verifie_probleme_carres(grille: Grille) -> bool:
    """Vérifie si un des sous carrés contient une répétition.

    Exemple:
    >>> valeurs = [None for _ in range(16)]
    >>> valeurs[0], valeurs[5] = 1, 1
    >>> _verifie_probleme_carres(grille=Grille(cases=valeurs))
    True
    """
    for indice_carre in (0, 2, 8, 10):
        if _doublon_present(
            [grille[indice_carre + indice_interne] for indice_interne in (0, 1, 4, 5)]
        ):
            return True
    return False


def est_valide(grille: Grille) -> bool:
    """Vérifie si la grille est valide.

    Exemple:
    >>> grille1 = Grille(cases=[None for _ in range(16)])
    >>> est_valide(grille1)
    True
    >>> grille2 = Grille(cases=[1, 2, 3, 4, None, 4, 1, 2, 2, None, None, None, 4, 3, 2, 1])
    >>> est_valide(grille2)
    True"""
    if _verifie_probleme_lignes(grille):
        return False
    if _verifie_probleme_colonnes(grille):
        return False
    if _verifie_probleme_carres(grille):
        return False
    return True


def est_complete(grille: Grille) -> bool:
    """Vérifie si toutes les cases sont remplies.

    Exemple:
    >>> grille_vide = Grille(cases=[None for _ in range(16)])
    >>> est_complete(grille_vide)
    False
    >>> grille_pleine = Grille(cases=[1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1])
    >>> est_complete(grille_pleine)
    True
    """
    for case in grille:
        if case is None:
            return False
    return True


def _cherche_premier_none(valeurs: list[Optional[int]]) -> int:
    """Renvoie l'indice du premier élément valant None.

    Génère une exception si il n'y a pas de None.

    Exemple:
    >>> _cherche_premier_none([None, 1, 2])
    0
    >>> _cherche_premier_none([1, None, 1, 2])
    1
    >>> _cherche_premier_none([None, 1, None, 2])
    0
    >>> _cherche_premier_none([1, 2, 3])
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "./lib.py", line 143, in _cherche_premier_none

    ValueError: Il n'y a pas de None dans cette liste.
    """
    for indice, valeur in enumerate(valeurs):
        if valeur is None:
            return indice
    raise ValueError("Il n'y a pas de None dans cette liste.")


def _remplit_une_case(grille: Grille) -> Generator[Grille, None, None]:
    """Renvoie un itérateurs des nouvelles grilles en remplissant la première case vide avec 1, 2, 3 puis 4.

    Exemple:
    >>> test = Grille(cases=[None for _ in range(16)])
    >>> print(test)

    -----------------
    | _ | _ | _ | _ |
    -----------------
    | _ | _ | _ | _ |
    -----------------
    | _ | _ | _ | _ |
    -----------------
    | _ | _ | _ | _ |
    -----------------

    >>> for nouvelle in _remplit_une_case(grille=test):
    ...     print(nouvelle)
    ...

    -----------------
    | 1 | _ | _ | _ |
    -----------------
    | _ | _ | _ | _ |
    -----------------
    | _ | _ | _ | _ |
    -----------------
    | _ | _ | _ | _ |
    -----------------


    -----------------
    | 2 | _ | _ | _ |
    -----------------
    | _ | _ | _ | _ |
    -----------------
    | _ | _ | _ | _ |
    -----------------
    | _ | _ | _ | _ |
    -----------------


    -----------------
    | 3 | _ | _ | _ |
    -----------------
    | _ | _ | _ | _ |
    -----------------
    | _ | _ | _ | _ |
    -----------------
    | _ | _ | _ | _ |
    -----------------


    -----------------
    | 4 | _ | _ | _ |
    -----------------
    | _ | _ | _ | _ |
    -----------------
    | _ | _ | _ | _ |
    -----------------
    | _ | _ | _ | _ |
    -----------------
    """
    cases = [case for case in grille]
    try:
        indice = _cherche_premier_none(cases)
    except ValueError:
        pass
    else:
        nouvelle = cases[:]
        for valeur in range(1, 5):
            nouvelle[indice] = valeur
            yield Grille(cases=nouvelle)


def _remplit_une_case_liste(grille: Grille) -> list[Grille]:
    """Version obsolète renvoyant une liste."""
    cases = [case for case in grille]
    try:
        indice = _cherche_premier_none(cases)
    except ValueError:
        return []
    nouvelles = [cases[:] for _ in range(4)]
    for valeur, nouvelle in zip(range(1, 5), nouvelles):
        nouvelle[indice] = valeur
    return [Grille(cases=nouvelle) for nouvelle in nouvelles]


def calcule_solutions(grille: Grille) -> list[Grille]:
    """Fonction renvoyant la liste des toutes les solutions correspondant à une grille partiellement remplie.

    Exemple:
    >>> calcule_solutions(grille=Grille(cases=[1, 2, 3, 4, 4, None, 2, 1, 2, 1, None, 3, 3, None, 1, 2]))
    [Grille(cases=[1, 2, 3, 4, 4, 3, 2, 1, 2, 1, 4, 3, 3, 4, 1, 2])]
    >>> calcule_solutions(grille=Grille(cases=[1, 2, 3, 4, 4, 1, 2, 1, 2, 1, None, 3, 3, None, 1, 2]))
    []"""
    if not est_valide(grille):
        return []
    if est_complete(grille):
        return [grille]
    resultat = list()
    for sous_grille in _remplit_une_case(grille):
        resultat.extend(calcule_solutions(grille=sous_grille))
    return resultat
