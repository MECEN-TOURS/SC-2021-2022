#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Script effectuant la répartition des sujets au élèves.
"""
import random as rd
from rich.console import Console

GROUPES = (
    ("Baptiste Nepveux", "Mathieu Veron"),
    ("Alexandre Jeanne", " Pierre Larcher"),
    ("Maurine Diot", " Laeticia Miguel"),
    ("Toky Cédric Lebon", " Julien Remondeau"),
    ("Tasnim El Tahir", " Ilona Rateau"),
    ("Léa Brasseur", " Benjamin Chauvet"),
    ("Dragomir Gudumac", " Verne Vincent"),
    ("Thomas Bisson", " Alexis Vialatte"),
    ("Anne-Sophie Nunes", " Manon Valliot", " Merve Yildirim"),
)

SUJETS = [f"{numero+1:02}" for numero in range(1, 14)]
rd.seed(2022)
rd.shuffle(SUJETS)

CS = Console()

AFFECTATION = {eleve: sujet for eleve, sujet in zip(GROUPES, SUJETS)}
CS.print(AFFECTATION)
