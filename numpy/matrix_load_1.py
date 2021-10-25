"""Přečtení obsahu matice ze standardního binárního souboru."""

import numpy as np

m = np.load("matrix1.npy")
print(m)
print(m.dtype)
