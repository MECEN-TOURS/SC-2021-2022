"""Description.

Tests automatiques de  la librairie.
"""
import pytest
from lib import (
    Grille,
    _case_valide,
    est_valide,
    _doublon_present,
    _verifie_probleme_lignes,
    _verifie_probleme_colonnes,
    _verifie_probleme_carres,
    est_complete,
    remplit_une_case,
    calcule_solutions,
    _cherche_premier_none,
)


def test_case_valide():
    assert _case_valide(1)
    assert _case_valide(2)
    assert _case_valide(3)
    assert _case_valide(4)
    assert _case_valide(None)
    assert not _case_valide(5)
    assert not _case_valide("1")
    assert not _case_valide(-1)


def test_grille_initialisation():
    cases = [None for _ in range(16)]
    grille = Grille(cases=cases)
    assert isinstance(grille, Grille)


def test_grille_initialisation_mauvaise_longueur():
    with pytest.raises(ValueError):
        Grille(cases=[])


def test_grille_initialisation_mauvaise_valeur():
    cases = [None for _ in range(16)]
    cases[-1] = 5
    with pytest.raises(ValueError):
        Grille(cases)


def test_grille_str():
    grille = Grille([1, 2, 3, 4, None, 4, 1, 2, 2, None, None, None, 4, 3, 2, 1])
    resultat = str(grille)
    attendu = """
-----------------
| 1 | 2 | 3 | 4 |
-----------------
| _ | 4 | 1 | 2 |
-----------------
| 2 | _ | _ | _ |
-----------------
| 4 | 3 | 2 | 1 |
-----------------
"""
    assert resultat == attendu


def test_grille_repr():
    grille = Grille(cases=[1, 2, 3, 4, None, 4, 1, 2, 2, None, None, None, 4, 3, 2, 1])
    resultat = repr(grille)
    attendu = (
        "Grille(cases=[1, 2, 3, 4, None, 4, 1, 2, 2, None, None, None, 4, 3, 2, 1])"
    )
    assert resultat == attendu


def test_grille_iter():
    valeurs = [1, 2, 3, 4, None, 4, 1, 2, 2, None, None, None, 4, 3, 2, 1]
    grille = Grille(cases=valeurs)
    cases = [case for case in grille]
    assert cases == valeurs


def test_grille_egalite():
    grille1 = Grille(cases=[1, 2, 3, 4, 4, 3, 2, 1, 2, 1, 4, 3, 3, 4, 1, 2])
    grille2 = Grille(cases=[1, 2, 3, 4, 4, 3, 2, 1, 2, 1, 4, 3, 3, 4, 1, 2])
    assert grille1 is not grille2
    assert grille1 == grille2


def test_doublon_present():
    assert not _doublon_present(valeurs=[1, 2, 3])
    assert _doublon_present(valeurs=[1, 1, 2])


def test_doublon_present_None():
    assert not _doublon_present(valeurs=[None, None])


def test_est_valide():
    grille1 = Grille(cases=[None for _ in range(16)])
    assert est_valide(grille1)
    valeurs = [1, 2, 3, 4, None, 4, 1, 2, 2, None, None, None, 4, 3, 2, 1]
    grille2 = Grille(cases=valeurs)
    assert est_valide(grille2)


def test_verifie_probleme_lignes():
    valeurs = [None for _ in range(16)]
    valeurs[0] = 1
    valeurs[1] = 1
    grille = Grille(cases=valeurs)
    assert _verifie_probleme_lignes(grille)


def test_verifie_probleme_colonnes():
    valeurs = [None for _ in range(16)]
    valeurs[0] = 1
    valeurs[4] = 1
    grille = Grille(cases=valeurs)
    assert _verifie_probleme_colonnes(grille)


def test_verifie_probleme__carres():
    valeurs = [None for _ in range(16)]
    valeurs[0] = 1
    valeurs[5] = 1
    grille = Grille(cases=valeurs)
    assert _verifie_probleme_carres(grille)


def test_est_complete():
    grille_vide = Grille(cases=[None for _ in range(16)])
    assert not est_complete(grille_vide)

    grille_pleine = Grille(cases=[1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1])
    assert est_complete(grille_pleine)


def test_remplit_une_case_cas_complet():
    grille_pleine = Grille(cases=[1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1])
    assert remplit_une_case(grille=grille_pleine) == []

def test_remplit_une_case():
    grille_depart = Grille(
        cases=[1, 2, 3, 4, 4, None, 2, 1, 2, 1, None, 3, 3, None, 1, 2]
    )
    assert list(remplit_une_case(grille=grille_depart)) == [
        Grille(cases=[1, 2, 3, 4, 4, 1, 2, 1, 2, 1, None, 3, 3, None, 1, 2]),
        Grille(cases=[1, 2, 3, 4, 4, 2, 2, 1, 2, 1, None, 3, 3, None, 1, 2]),
        Grille(cases=[1, 2, 3, 4, 4, 3, 2, 1, 2, 1, None, 3, 3, None, 1, 2]),
        Grille(cases=[1, 2, 3, 4, 4, 4, 2, 1, 2, 1, None, 3, 3, None, 1, 2]),
    ]

def test_remplit_une_case_liste():
    grille_depart = Grille(
        cases=[1, 2, 3, 4, 4, None, 2, 1, 2, 1, None, 3, 3, None, 1, 2]
    )
    assert remplit_une_case(grille=grille_depart) == [
        Grille(cases=[1, 2, 3, 4, 4, 1, 2, 1, 2, 1, None, 3, 3, None, 1, 2]),
        Grille(cases=[1, 2, 3, 4, 4, 2, 2, 1, 2, 1, None, 3, 3, None, 1, 2]),
        Grille(cases=[1, 2, 3, 4, 4, 3, 2, 1, 2, 1, None, 3, 3, None, 1, 2]),
        Grille(cases=[1, 2, 3, 4, 4, 4, 2, 1, 2, 1, None, 3, 3, None, 1, 2]),
    ]


def test_cherche_premier_none():
    assert _cherche_premier_none([None, 1, 2]) == 0
    assert _cherche_premier_none([1, None, 1, 2]) == 1
    assert _cherche_premier_none([None, 1, None, 2]) == 0


def test_cherche_premier_none_impossible():
    with pytest.raises(ValueError):
        _cherche_premier_none([1, 2, 3])


def test_calcule_solutions_positif():
    assert calcule_solutions(
        grille=Grille(cases=[1, 2, 3, 4, 4, None, 2, 1, 2, 1, None, 3, 3, None, 1, 2])
    ) == [Grille(cases=[1, 2, 3, 4, 4, 3, 2, 1, 2, 1, 4, 3, 3, 4, 1, 2])]


def test_calcule_solutions_negatif():
    assert (
        calcule_solutions(
            grille=Grille(cases=[1, 2, 3, 4, 4, 1, 2, 1, 2, 1, None, 3, 3, None, 1, 2])
        )
        == []
    )
