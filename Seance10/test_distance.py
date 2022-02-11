"""Description.

Tests automatiques de lib_distance.
"""
import pytest
from lib_graphe import Graphe
from lib_distance import (_calcule_suivante, calcule_distance )

@pytest.fixture
def graphe():
    return Graphe(
        sommets=["a", "b", "c", "d"],
        arretes=[
            ("a", "b", 1),
            ("b", "a", 1),
            ("a", "c", 5),
            ("c", "a", 5), 
            ("b", "c", 3),
            ("c", "b", 3),
            ("b", "d", 1),
            ("d", "b", 1),
            ("c", "d", 1),
            ("d", "c", 1),
        ]
    )

def test_calcule_suivante(graphe):
    d0 = {"a": 0.0, "b": float("inf"), "c": float("inf"), "d": float("inf")}
    d1 = {"a": 0.0, "b": 1.0, "c": 5.0, "d": float("inf")}
    d2 = {"a": 0.0, "b": 1.0, "c": 4.0, "d": 2.0}
    d3 = {"a": 0.0, "b": 1.0, "c": 3.0, "d": 2.0}
    d4 = {"a": 0.0, "b": 1.0, "c": 3.0, "d": 2.0}
    assert _calcule_suivante(graphe, "a", d0) == d1
    assert _calcule_suivante(graphe, "a", d1) == d2
    assert _calcule_suivante(graphe, "a", d2) == d3
    assert _calcule_suivante(graphe, "a", d3) == d4
    
def test_calcule_distance(graphe):
    assert calcule_distance(graphe, "a", "c") == 3.0