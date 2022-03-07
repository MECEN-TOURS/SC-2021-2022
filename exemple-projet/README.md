# Exemple de projet

On va développer une application permettant de résoudre une classe de problème comprenant, entre autre, le problème de traversée  de rivière.

## Description

On a une librairie `final` doublée d'une interface en ligne de commande (via le script `__main__.py`).
On a deux commandes.

### Exemple

On peut d'abord générer un exemple de fichier décrivant l'exemple correspondant à la traversée du berger, loup, mouton et chou via.

```sh
python -m final exemple donnees.json
```

On aura alors **généré** un fichier `donnees.json`.
On pourra ensuite le modifier pour décrire un nouveau problème.

### Calcule

On peut aussi chercher à résoudre un problème de ce type, encodé dans in fichier (ici `probleme.json`).

```sh
python -m final calcule probleme.json
```

## Remarques

On a introduit ici des nouvelles librairies.

1. [`poetry`](https://python-poetry.org/) pour gérer les dépendances, la structure du projet et un environnement virtuel. On pourrait aussi s'en servir pour déployer le paquet sur pypi.
2. [`pyserde`](https://yukinarit.github.io/pyserde/guide/) pour sérialiser/désérialiser les objets permettant de décrire un problème spécifique.
3. [`typer`](https://typer.tiangolo.com/) qui permet rapidement de créer une application en ligne de commande à partir de simple fonctions.
4. [`rich`](https://rich.readthedocs.io/en/stable/introduction.html) pour un affichage plus lisible et esthétique en sortie.

Les dépendances de développement sont

1. [pytest](https://docs.pytest.org/en/7.0.x/) pour avoir des tests automatiques de la librairie.
2. [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) pour analyser la couverture des tests.
3. [black](https://black.readthedocs.io/en/stable/) pour standardiser le style du code.
4. [pylama](https://klen.github.io/pylama/) pour l'analyse syntaxique du code.
