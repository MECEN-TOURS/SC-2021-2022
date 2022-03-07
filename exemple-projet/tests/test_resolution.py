from final.data import Donnees
from final.resolution import resoud
from final.conversion import Cote

import pytest

def test_resoud_bateau():
    essai = Donnees(
        personnages=["Berger", "Loup"],
        nb_places=2,
        rameurs=["Berger"],
        contraintes=[],
    )
    assert resoud(essai) == [
        {"Berger": Cote.GAUCHE, "Loup": Cote.GAUCHE},
        {"Berger": Cote.DROIT, "Loup": Cote.DROIT},
    ]
    
def test_resoud_echec():
    essai = Donnees(
        personnages=["Berger", "Loup"],
        nb_places=1,
        rameurs=["Berger"],
        contraintes=[],
    )
    with pytest.raises(ValueError):
        resoud(essai)