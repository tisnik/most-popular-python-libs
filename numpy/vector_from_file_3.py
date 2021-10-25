"""Načtení obsahu vektoru z binárního souboru (nekorektní použití)."""

import numpy as np

v = np.fromfile("vector4.bin")
print(v)
