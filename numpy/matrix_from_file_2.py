"""Načtení obsahu matice z textového souboru se specifikací oddělovače."""

import numpy as np

m = np.fromfile("matrix1.txt", sep=",").reshape(3, 4).astype("b")
print(m)
