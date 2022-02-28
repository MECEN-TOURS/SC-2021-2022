"""Description.

Tests automatiques associés à la conversion.
"""
import pytest
import numpy as np
from lib_conversion import Tableaux, convertit
from lib_probleme import Probleme

def test_tableaux():
    essai = Tableaux(
        l = np.zeros(shape=(8,)),
        u = np.array([4., 1, 2, 3, 2, 1, 2, 2]),
        Aeq = np.array(
            [
                [1, 0, -1, -1, 0, 0, 0, 0], 
                [0, 0, 0, 1, -1, 1, 0, 0], 
                [0, 1, 0, 0, 0, -1, -1, 0], 
                [0, 0, 0, 0, 0, 0, 1, -1]
            ]
        ),
        beq=np.zeros(shape=(4,)),
        c=np.array([-1, -1, 0, 0, 0, 0, 0, 0]),
    )
    assert isinstance(essai, Tableaux)
    
def test_dimensions_tableaux():
    with pytest.raises(ValueError):
        Tableaux(
            l = np.zeros(shape=(9,)),
            u = np.array([4., 1, 2, 3, 2, 1, 2, 2]),
            Aeq = np.array(
                [
                    [1, 0, -1, -1, 0, 0, 0, 0], 
                    [0, 0, 0, 1, -1, 1, 0, 0], 
                    [0, 1, 0, 0, 0, -1, -1, 0], 
                    [0, 0, 0, 0, 0, 0, 1, -1]
                ]
            ),
            beq=np.zeros(shape=(4,)),
            c=np.array([-1, -1, 0, 0, 0, 0, 0, 0]),
        )
    with pytest.raises(ValueError):
        Tableaux(
            l = np.zeros(shape=(8,)),
            u = np.array([4., 1, 2, 3, 2, 1, 2, 2]),
            Aeq = np.array(
                [
                    [1, 0, -1, -1, 0, 0, 0, 0], 
                    [0, 0, 0, 1, -1, 1, 0, 0], 
                    [0, 1, 0, 0, 0, -1, -1, 0], 
                    [0, 0, 0, 0, 0, 0, 1, -1]
                ]
            ),
            beq=np.zeros(shape=(4,)),
            c=np.array([-1, -1, 0, 0, 0, 0, 0, 0, 0]),
        )
    with pytest.raises(ValueError):
        Tableaux(
            l = np.zeros(shape=(8,)),
            u = np.array([4., 1, 2, 3, 2, 1, 2, 2]),
            Aeq = np.array(
                [
                    [1, 0, -1, -1, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 1, -1, 1, 0, 0, 0], 
                    [0, 1, 0, 0, 0, -1, -1, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 1, -1, 0]
                ]
            ),
            beq=np.zeros(shape=(4,)),
            c=np.array([-1, -1, 0, 0, 0, 0, 0, 0]),
        )
    with pytest.raises(ValueError):
        Tableaux(
            l = np.zeros(shape=(8,)),
            u = np.array([4., 1, 2, 3, 2, 1, 2, 2]),
            Aeq = np.array(
                [
                    [1, 0, -1, -1, 0, 0, 0, 0], 
                    [0, 0, 0, 1, -1, 1, 0, 0], 
                    [0, 1, 0, 0, 0, -1, -1, 0], 
                    [0, 0, 0, 0, 0, 0, 1, -1]
                ]
            ),
            beq=np.zeros(shape=(5,)),
            c=np.array([-1, -1, 0, 0, 0, 0, 0, 0]),
        )


def test_convertit():
    probleme = Probleme(
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
    attendu = Tableaux(
        l = np.zeros(shape=(8,)),
        u = np.array([4., 1, 2, 3, 2, 1, 2, 2]),
        Aeq = np.array(
            [
                [1, 0, -1, -1, 0, 0, 0, 0], 
                [0, 0, 0, 1, -1, 1, 0, 0], 
                [0, 1, 0, 0, 0, -1, -1, 0], 
                [0, 0, 0, 0, 0, 0, 1, -1]
            ]
        ),
        beq=np.zeros(shape=(4,)),
        c=np.array([-1, -1, 0, 0, 0, 0, 0, 0]),
    )
    assert convertit(probleme) == attendu