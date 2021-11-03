"""Uložení více matic do standardního binárního souboru."""

import numpy as np

# rozměry matice
rows = 1000
columns = 1000

# vytvoření větší matice o zadaném tvaru
m0 = np.zeros((rows, columns), dtype="i")

# uložení matice do souboru ve standardním formátu
np.savez("matrix_uncompressed.npz", m0)

# uložení matice do souboru ve standardním zkomprimovaném formátu
np.savez_compressed("matrix_compressed.npz", m0)
