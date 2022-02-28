"""Description.

Tests automatiques de la classe Probleme.
"""
import pytest
from lib_probleme import Probleme

def test_init():
    essai = Probleme(
        sommets=["A", "B", "C", "D", "P", "S"],
        arretes=[
            ("S", "A", 4), 
            ("S", "C", 1), 
            ("A", "P", 2), 
            ("A", "B", 3), 
            ("B", "P", 2),
            ("C", "B", 1),
            ("C", "D", 2),
            ("D", "P", 2),
        ],
        source="S",
        puit="P",
    )
    assert isinstance(essai, Probleme)
    
def test_init_puit_source():
    with pytest.raises(ValueError):
        Probleme(sommets=["A", "B"], arretes=[("A", "B", 1)], source="C", puit="B")
    with pytest.raises(ValueError):
        Probleme(sommets=["A", "B"], arretes=[("A", "B", 1)], source="A", puit="D")
    

def test_repr():
    essai = Probleme(sommets=["A", "B"], arretes=[("A", "B", 1)], source="A", puit="B")
    assert repr(essai) == """Probleme(sommets=['A', 'B'], arretes=[('A', 'B', 1.0)], source='A', puit='B')"""
    
def test_egalite():
    essai1 = Probleme(
        sommets=["A", "B", "C", "D", "P", "S"],
        arretes=[
            ("S", "A", 4.), 
            ("S", "C", 1.), 
            ("A", "P", 2), 
            ("A", "B", 3), 
            ("B", "P", 2),
            ("C", "B", 1),
            ("C", "D", 2),
            ("D", "P", 2),
        ],
        source="S",
        puit="P",
    )
    essai2 = Probleme(
        sommets=["A", "B", "C", "D", "S", "P"],
        arretes=[
            ("S", "A", 4), 
            ("A", "P", 2), 
            ("S", "C", 1), 
            ("A", "B", 3), 
            ("B", "P", 2),
            ("C", "B", 1),
            ("C", "D", 2),
            ("D", "P", 2),
        ],
        source="S",
        puit="P",
    )
    assert essai1 == essai2