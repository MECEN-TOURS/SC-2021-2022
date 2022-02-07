"""Description.

Tests automatiques de lib_graphe.
"""
import pytest
from lib_graphe import (Graphe, genere_dot, genere_graphe, _gere_ligne)

def test_init():
    exemple = Graphe(sommets=["a", "b", "c"], arretes=[("a", "b"), ("a", "c")])
    assert isinstance(exemple, Graphe)
    
def test_repr():
    exemple = Graphe(sommets=["a", "b", "c"], arretes=[("a", "b"), ("a", "c")])
    attendu = "Graphe(sommets=['a', 'b', 'c'], arretes=[('a', 'b'), ('a', 'c')])"
    assert repr(exemple) == attendu
    
def test_egalite_naive():
    exemple1 = Graphe(sommets=["a", "b", "c"], arretes=[("a", "b"), ("a", "c")])
    exemple2 = Graphe(sommets=["a", "b", "c"], arretes=[("a", "b"), ("a", "c")])
    assert exemple1 == exemple2
    
def test_egalite():
    exemple1 = Graphe(sommets=["a", "b", "c"], arretes=[("a", "b"), ("a", "c")])
    exemple2 = Graphe(sommets=["a", "c", "b"], arretes=[("a", "c"), ("a", "b")])
    assert exemple1 == exemple2  
    
def test_iteration():
    exemple = Graphe(sommets=["a", "b", "c"], arretes=[("a", "b"), ("a", "c")])
    ex = iter(exemple)
    next(ex) == ("a", "b")
    next(ex) == ("a", "c")
    with pytest.raises(StopIteration):
        next(ex)


def test_genere_dot():
    exemple = Graphe(sommets=["a", "b", "c"], arretes=[("a", "b"), ("a", "c")])
    attendu = """
digraph {
a -> b;
a -> c;
}
"""
    assert genere_dot(graphe=exemple) == attendu

    
def test_gere_ligne():
    assert _gere_ligne(ligne="A -> B;") == ("A", "B")
    
    
    
def test_genere_graphe():
    exemple = Graphe(sommets=["a", "b", "c"], arretes=[("a", "b"), ("a", "c")])
    code = genere_dot(graphe=exemple)
    resultat = genere_graphe(code_dot=code)
    assert exemple == resultat