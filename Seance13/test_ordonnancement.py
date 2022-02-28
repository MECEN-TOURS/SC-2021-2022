"""Description.

Tests automatique de la librairie ordonnancement.
"""

from ordonnancement import ordonnance, _cherche_sans_prerequis, _elague_cdc, edt_parallele

def test_elague_cdc():
    cdc = {
        "A": ["B", "C"], 
        "B": ["E"],
        "C": ["B"],
        "D": ["A", "E"],
        "E": [],
        "F": ["C", "D"],
        "G": ["A", "I", "J"],
        "H": ["G", "J"],
        "I": ["C"],
        "J": ["A"],
    }
    attendu = {
        "A": ["B", "C"], 
        "B": [],
        "C": ["B"],
        "D": ["A"],
        "F": ["C", "D"],
        "G": ["A", "I", "J"],
        "H": ["G", "J"],
        "I": ["C"],
        "J": ["A"],
    }
    assert attendu == _elague_cdc(cahier_des_charges=cdc, a_effectuer="E")
    
def test_ordonnance_complet():
    donnees = {
        "A": ["B", "C"], 
        "B": ["E"],
        "C": ["B"],
        "D": ["A", "E"],
        "E": [],
        "F": ["C", "D"],
        "G": ["A", "I", "J"],
        "H": ["G", "J"],
        "I": ["C"],
        "J": ["A"],
    }
    attendu = ["E", "B", "C", "A", "D", "F", "I", "J", "G", "H"]
    assert attendu == ordonnance(donnees)
    
def test_cherche_sans_prerequis():
    donnees = {
        "A": ["B", "C"], 
        "B": ["E"],
        "C": ["B"],
        "D": ["A", "E"],
        "E": [],
        "F": ["C", "D"],
        "G": ["A", "I", "J"],
        "H": ["G", "J"],
        "I": ["C"],
        "J": ["A"],
    }
    attendu = ["E"]
    assert attendu == _cherche_sans_prerequis(donnees)
    
def test_edt():
    donnees = {
        "A": (["B", "C"], 1), 
        "B": (["E"], 2),
        "C": (["B"], 3),
        "D": (["A", "E"], 2),
        "E": ([], 3),
        "F": (["C", "D"], 2),
        "G": (["A", "I", "J"], 1),
        "H": (["G", "J"], 2),
        "I": (["C"], 2),
        "J": (["A"], 4),
    }
    attendu = {
        "E": (0, 3),
        "B": (3, 5),
        "C": (5, 8),
        "A": (8, 9),
        "D": (9, 11),
        "F": (11, 13),
        "I": (8, 10),
        "J": (9, 13),
        "G": (13, 14),
        "H": (14, 16),
    }
    assert edt_parallele(donnees) == attendu