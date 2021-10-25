"""Načtení obsahu datové řady z binárního souboru s konverzí."""

import numpy as np
import pandas as pd

v = np.fromfile("vector4.bin", dtype="h")
s = pd.Series(v)

print(s)
print()
print(s.describe())
