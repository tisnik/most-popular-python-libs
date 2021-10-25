"""Přečtení obsahu vektoru ze standardního binárního souboru."""

import numpy as np

v = np.load("vector.npy")
print(v)
print(v.dtype)
