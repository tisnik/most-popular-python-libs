"""Uložení obsahu matice do standardního binárního souboru."""

import numpy as np

m = np.linspace(1, 12, 12, dtype="f").reshape(3, 4)
print(m)

np.save("matrix2.npy", m, allow_pickle=False)
