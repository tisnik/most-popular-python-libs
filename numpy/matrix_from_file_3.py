"""Načtení obsahu matice z binárního souboru bez specifikace formátu."""

import numpy as np

m = np.fromfile("matrix2.bin").reshape(3, 4)
print(m)
