"""Přečtení obsahu matice ze standardního binárního souboru."""

import numpy as np

m = np.load("matrix2.npy")
print(m)
print(m.dtype)
