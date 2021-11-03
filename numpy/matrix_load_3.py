"""Přečtení obsahu matice ze standardního binárního souboru."""

import numpy as np

# načtení matice ze standardního binárního souboru
m = np.load("matrix3.npy")

# zobrazení obsahu matice
print(m)
print()

# zobrazení dalších informací o matici
print("Dimensions:", m.ndim)
print("Data type:", m.dtype)
print("Item size:", m.itemsize, "bytes")
print("Array size:", m.size, "items")
