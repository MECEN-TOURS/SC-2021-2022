from final.data import Donnees
from final.conversion import _genere_etats, Cote, _verifie_contrainte, _genere_sommets, _sont_relies, convertit
import pytest

def test_genere_etats():
    entree = Donnees(
            personnages=["Berger", "Loup"],
            nb_places=2,
            rameurs=["Berger"],
            contraintes=[],
        )
    attendu = [
        {"Berger": Cote.GAUCHE, "Loup": Cote.GAUCHE},
        {"Berger": Cote.GAUCHE, "Loup": Cote.DROIT},
        {"Berger": Cote.DROIT, "Loup": Cote.GAUCHE},
        {"Berger": Cote.DROIT, "Loup": Cote.DROIT},
    ]
    assert _genere_etats(entree) == attendu
    
def test_verifie_contrainte():
    contrainte = ("Berger", ["Loup", "Mouton"])
    etat1 = {"Berger": Cote.GAUCHE, "Loup": Cote.DROIT, "Mouton": Cote.DROIT}
    assert not _verifie_contrainte(etat1, contrainte)
    etat2 = {"Berger": Cote.DROIT, "Loup": Cote.DROIT, "Mouton": Cote.DROIT}
    assert _verifie_contrainte(etat2, contrainte)
    etat2 = {"Berger": Cote.DROIT, "Loup": Cote.GAUCHE, "Mouton": Cote.DROIT}
    assert _verifie_contrainte(etat2, contrainte)
    
def test_genere_sommets():
    donnees = Donnees(
        personnages=["Berger", "Loup", "Mouton"],
        nb_places=2,
        rameurs=["Berger"],
        contraintes=[
            ("Berger", ["Loup", "Mouton"]),
        ],
    )
    attendu = [
        {"Berger": Cote.GAUCHE, "Loup": Cote.GAUCHE, "Mouton": Cote.GAUCHE},
        {"Berger": Cote.GAUCHE, "Loup": Cote.GAUCHE, "Mouton": Cote.DROIT},
        {"Berger": Cote.GAUCHE, "Loup": Cote.DROIT, "Mouton": Cote.GAUCHE},
        {"Berger": Cote.DROIT, "Loup": Cote.GAUCHE, "Mouton": Cote.DROIT},
        {"Berger": Cote.DROIT, "Loup": Cote.DROIT, "Mouton": Cote.GAUCHE},
        {"Berger": Cote.DROIT, "Loup": Cote.DROIT, "Mouton": Cote.DROIT},
    ]
    assert _genere_sommets(donnees) == attendu
    
def test_sont_relies():
    donnees = Donnees(
        personnages=["Berger", "Loup", "Mouton"],
        nb_places=2,
        rameurs=["Berger"],
        contraintes=[
            ("Berger", ["Loup", "Mouton"]),
        ],
    )
    assert _sont_relies(
        depart={"Berger": Cote.GAUCHE, "Loup": Cote.GAUCHE, "Mouton": Cote.GAUCHE},
        arrivee={"Berger": Cote.DROIT, "Loup": Cote.DROIT, "Mouton": Cote.GAUCHE},
        donnees=donnees,
    )
    assert not _sont_relies(
        depart={"Berger": Cote.GAUCHE, "Loup": Cote.GAUCHE, "Mouton": Cote.GAUCHE},
        arrivee={"Berger": Cote.GAUCHE, "Loup": Cote.DROIT, "Mouton": Cote.DROIT},
        donnees=donnees,
    )
    assert not _sont_relies(
        depart={"Berger": Cote.GAUCHE, "Loup": Cote.GAUCHE, "Mouton": Cote.GAUCHE},
        arrivee={"Berger": Cote.DROIT, "Loup": Cote.DROIT, "Mouton": Cote.DROIT},
        donnees=donnees,
    )
    assert not _sont_relies(
        depart={"Berger": Cote.GAUCHE, "Loup": Cote.DROIT, "Mouton": Cote.GAUCHE},
        arrivee={"Berger": Cote.DROIT, "Loup": Cote.GAUCHE, "Mouton": Cote.GAUCHE},
        donnees=donnees,
    )
    
def test_conversion():
    donnees = Donnees(
        personnages=["Berger", "Loup"],
        nb_places=1,
        rameurs=["Berger"],
        contraintes=[],
    )
    assert convertit(donnees) == (
        [
            {"Berger": Cote.GAUCHE, "Loup": Cote.GAUCHE}, 
            {"Berger": Cote.GAUCHE, "Loup": Cote.DROIT},
            {"Berger": Cote.DROIT, "Loup": Cote.GAUCHE},
            {"Berger": Cote.DROIT, "Loup": Cote.DROIT},
        ],
        [
            ({"Berger": Cote.GAUCHE, "Loup": Cote.GAUCHE}, {"Berger": Cote.DROIT, "Loup": Cote.GAUCHE}),
            ({"Berger": Cote.GAUCHE, "Loup": Cote.DROIT}, {"Berger": Cote.DROIT, "Loup": Cote.DROIT}),
            ({"Berger": Cote.DROIT, "Loup": Cote.GAUCHE}, {"Berger": Cote.GAUCHE, "Loup": Cote.GAUCHE}),
            ({"Berger": Cote.DROIT, "Loup": Cote.DROIT}, {"Berger": Cote.GAUCHE, "Loup": Cote.DROIT}),
        ]
    )