"""Description.

Tests automatiques de la librairie de resolution.
"""
import pytest
from lib_resolution import Solution, resout
from lib_probleme import Probleme


def test_init():
    essai = Solution(
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
    assert isinstance(essai, Solution)
    
def test_init_puit_source():
    with pytest.raises(ValueError):
        Solution(sommets=["A", "B"], arretes=[("A", "B", 1)], source="C", puit="B")
    with pytest.raises(ValueError):
        Solution(sommets=["A", "B"], arretes=[("A", "B", 1)], source="A", puit="D")
    

def test_repr():
    essai = Solution(sommets=["A", "B"], arretes=[("A", "B", 1)], source="A", puit="B")
    assert repr(essai) == """Solution(sommets=['A', 'B'], arretes=[('A', 'B', 1.0)], source='A', puit='B')"""
    
def test_egalite():
    essai1 = Solution(
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
    essai2 = Solution(
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
    
def test_resout():
    entree = Probleme(
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
    attendu = Solution(
        sommets=["A", "B", "C", "D", "P", "S"],
        arretes=[
            ("S", "A", 4), 
            ("S", "C", 1), 
            ("A", "P", 2), 
            ("A", "B", 2), 
            ("B", "P", 2),
            ("C", "B", 0),
            ("C", "D", 1),
            ("D", "P", 1),
        ],
        source="S",
        puit="P",
    )
    assert resout(entree) == attendu