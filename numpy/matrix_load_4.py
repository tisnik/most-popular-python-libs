"""Přečtení obsahu matice ze standardního binárního souboru."""

import numpy as np

# použití režimu mmap
m = np.load("matrix3.npy", mmap_mode="r")

# zobrazení dalších informací o matici
print("Dimensions:", m.ndim)
print("Data type:", m.dtype)
print("Item size:", m.itemsize, "bytes")
print("Array size:", m.size, "items")
