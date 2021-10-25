"""Načtení obsahu vektoru z binárního souboru s konverzí."""

import numpy as np

v = np.fromfile("vector4.bin", dtype="h")
print(v)
