"""Uložení obsahu matice do standardního binárního souboru."""

import numpy as np

# matice obsahující celočíselné 8bitové hodnoty (byte)
m = np.linspace(1, 12, 12, dtype="b").reshape(3, 4)
print(m)

np.save("matrix1.npy", m, allow_pickle=False)
