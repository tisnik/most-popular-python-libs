"""Načtení obsahu vektoru z textového souboru se specifikací oddělovače."""

import numpy as np

v = np.fromfile("vector1.txt", sep=",")
print(v)
