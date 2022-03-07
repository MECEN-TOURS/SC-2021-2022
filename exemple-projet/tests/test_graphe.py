"""Description.
Tests automatique de la librairie graphe.py
"""
import pytest
from final.graphes import (
    PasDeChemin,
    _calcule_voisins,
    _elague_sommets,
    _elague_arretes,
    calcule_chemin,
)


def test_calcule_voisins():
    attendu = [2, 3]
    sortie = _calcule_voisins(depart=1, arretes=[(1, 2), (1, 3)])
    assert sortie == attendu


def test_calcule_voisins_sans_boucle():
    attendu = [2, 3]
    sortie = _calcule_voisins(depart=1, arretes=[(1, 1), (1, 2), (1, 3)])
    assert sortie == attendu


def test_elague_sommets():
    attendu = [2, 3]
    calcule = _elague_sommets(a_enlever=1, sommets=[1, 2, 3])
    assert attendu == calcule


def test_elague_sommets_limite():
    calcule = _elague_sommets(a_enlever=4, sommets=[1, 2, 3])
    attendu = [1, 2, 3]
    assert calcule == attendu


def test_elague_arretes_negatif():
    calcule = _elague_arretes(a_enlever=1, arretes=[(1, 1), (1, 2), (1, 3)])
    attendu = []
    assert attendu == calcule


def test_elague_arretes_positif():
    calcule = _elague_arretes(a_enlever=1, arretes=[(1, 1), (1, 2), (1, 3), (2, 3)])
    attendu = [(2, 3)]
    assert attendu == calcule


def test_calcule_chemin_simple():
    calcule = calcule_chemin(
        depart=1,
        arrivee=4,
        sommets=[1, 2, 3, 4],
        arretes=[(1, 1), (1, 2), (1, 3), (2, 4)],
    )
    attendu = [1, 2, 4]
    assert attendu == calcule


def test_calcule_chemin_absent():
    with pytest.raises(PasDeChemin):
        calcule_chemin(
            depart=4,
            arrivee=1,
            sommets=[1, 2, 3, 4],
            arretes=[(1, 1), (1, 2), (1, 3), (2, 4)],
        )