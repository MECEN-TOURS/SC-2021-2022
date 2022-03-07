"""Description.

Test automatiques de data.
"""
from final.data import Donnees
import pytest

def test_donnees():
    essai = Donnees(
        personnages=["Berger", "Loup", "Mouton", "Choux"],
        nb_places=2,
        rameurs=["Berger"],
        contraintes=[
            ("Berger", ["Loup", "Mouton"]),
            ("Berger", ["Mouton", "Choux"]),
        ],
    )
    isinstance(essai, Donnees)
    
def test_donnees_problematiques():
    with pytest.raises(ValueError):
        Donnees(
            personnages=["Berger", "Loup", "Mouton", "Choux"],
            nb_places=0,
            rameurs=["Berger"],
            contraintes=[
                ("Berger", ["Loup", "Mouton"]),
                ("Berger", ["Mouton", "Choux"]),
            ],
        )
    with pytest.raises(ValueError):
        Donnees(
            personnages=["Berger", "Loup", "Mouton", "Choux"],
            nb_places=2,
            rameurs=["Bergers"],
            contraintes=[
                ("Berger", ["Loup", "Mouton"]),
                ("Berger", ["Mouton", "Choux"]),
            ],
        )
    with pytest.raises(ValueError):
        Donnees(
            personnages=["Berger", "Loup", "Mouton", "Choux"],
            nb_places=2,
            rameurs=["Berger"],
            contraintes=[
                ("Berge", ["Loup", "Mouton"]),
                ("Berger", ["Mouton", "Choux"]),
            ],
        )
    with pytest.raises(ValueError):
        Donnees(
            personnages=["Berger", "Loup", "Mouton", "Choux"],
            nb_places=2,
            rameurs=["Berger"],
            contraintes=[
                ("Berger", ["Loup", "Mouton"]),
                ("Berger", ["Mouton", "Chou"]),
            ],
        )
    
