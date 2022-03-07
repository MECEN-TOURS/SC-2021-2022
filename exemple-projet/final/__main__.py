"""Description.

Application ligne de commande pour la librairie de traversée de rivière.
"""

from .data import Donnees
from .resolution import resoud
from serde.json import from_json, to_json
import typer
from rich import print

application = typer.Typer()

@application.command()
def exemple(nom_fichier: str):
    exemple = Donnees(
        personnages=["Berger", "Loup", "Mouton", "Choux"],
        nb_places=2,
        rameurs=["Berger"],
        contraintes=[
            ("Berger", ["Loup", "Mouton"]),
            ("Berger", ["Mouton", "Choux"]),
        ],
    )

    code = to_json(exemple)

    with open(nom_fichier, "w") as fichier:
        fichier.write(code)
        
@application.command()
def calcule(nom_fichier: str):
    with open(nom_fichier, "r") as fichier:
        code = fichier.read()
        
    donnees = from_json(Donnees, code)
    solution = resoud(donnees)
    print(solution)
    
        
        
if __name__ == "__main__":
    application()