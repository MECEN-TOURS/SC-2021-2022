"""Description.

Tests automatiques de lib_graphe.
"""
import pytest
from lib_graphe import (
    Graphe,
    genere_dot,
    genere_graphe,
    _gere_ligne,
    _decoupe_interieur,
)


def test_init():
    exemple = Graphe(
        sommets=["a", "b", "c"], arretes=[("a", "b", 1.5), ("a", "c", 1.0)]
    )
    assert isinstance(exemple, Graphe)


def test_repr():
    exemple = Graphe(sommets=["a", "b", "c"], arretes=[("a", "b", 1), ("a", "c", 1.5)])
    attendu = (
        "Graphe(sommets=['a', 'b', 'c'], arretes=[('a', 'b', 1.0), ('a', 'c', 1.5)])"
    )
    assert repr(exemple) == attendu


def test_egalite_naive():
    exemple1 = Graphe(sommets=["a", "b", "c"], arretes=[("a", "b", 1.5), ("a", "c", 1)])
    exemple2 = Graphe(
        sommets=["a", "b", "c"], arretes=[("a", "b", 1.5), ("a", "c", 1.0)]
    )
    assert exemple1 == exemple2


def test_egalite():
    exemple1 = Graphe(
        sommets=["a", "b", "c"], arretes=[("a", "b", 1.5), ("a", "c", 0.5)]
    )
    exemple2 = Graphe(
        sommets=["a", "c", "b"], arretes=[("a", "c", 0.5), ("a", "b", 1.5)]
    )
    assert exemple1 == exemple2


def test_inegalite():
    exemple1 = Graphe(
        sommets=["a", "b", "c"], arretes=[("a", "b", 1.5), ("a", "c", 0.5)]
    )
    exemple2 = Graphe(
        sommets=["a", "c", "b"], arretes=[("a", "c", 0.5), ("a", "b", 1.0)]
    )
    assert exemple1 != exemple2


def test_iteration():
    exemple = Graphe(
        sommets=["a", "b", "c"], arretes=[("a", "b", 1.5), ("a", "c", 1)]
    )
    ex = iter(exemple)
    next(ex) == ("a", "b", 1.5)
    next(ex) == ("a", "c", 1.0)
    with pytest.raises(StopIteration):
        next(ex)
        
def test_sommets():
    exemple = Graphe(
        sommets=["a", "b", "c"], arretes=[("a", "b", 1.5), ("a", "c", 1)]
    )
    ex = iter(exemple.sommets())
    next(ex) == "a"
    next(ex) == "b"
    next(ex) == "c"
    with pytest.raises(StopIteration):
        next(ex)

def test_predecesseurs():
    exemple = Graphe(
        sommets=["a", "b", "c"], arretes=[("a", "b", 1.5), ("a", "c", 1), ("b", "a", 5.)]
    )
    pa = iter(exemple["a"])
    next(pa) == ("b", 5.0)
    with pytest.raises(StopIteration):
        next(pa)

def test_genere_dot():
    exemple = Graphe(sommets=["a", "b", "c"], arretes=[("a", "b", 1.5), ("a", "c", 1)])
    attendu = """
digraph {
a -> b [label=1.5];
a -> c [label=1.0];
}
"""
    assert genere_dot(graphe=exemple) == attendu


def test_gere_ligne():
    assert _gere_ligne(ligne="A -> B [label=1.5];") == ("A", "B", 1.5)
    assert _gere_ligne(ligne="premier -> deuxieme [label=1.5];") == ("premier", "deuxieme", 1.5)


def test_decoupe_interieur():
    entree = """
graph {
ligne1 [label=1.0];
ligne2 [label=1.5];
}
"""
    attendu = ["ligne1 [label=1.0];", "ligne2 [label=1.5];"]
    assert _decoupe_interieur(code=entree) == attendu


def test_genere_graphe():
    exemple = Graphe(
        sommets=["a", "b", "c"], arretes=[("a", "b", 1.0), ("a", "c", 1.5)]
    )
    code = genere_dot(graphe=exemple)
    resultat = genere_graphe(code_dot=code)
    assert exemple == resultat

    