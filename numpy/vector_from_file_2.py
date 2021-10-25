"""Načtení obsahu vektoru z textového souboru se specifikací oddělovače a s konverzí."""

import numpy as np

v = np.fromfile("vector1.txt", sep=",").astype("i")
print(v)
