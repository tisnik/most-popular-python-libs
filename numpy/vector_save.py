"""Uložení obsahu vektoru do standardního binárního souboru."""

import numpy as np

# vektor obsahující hodnoty s plovoucí řádovou čárkou
# s poloviční přesností (half)
v = np.linspace(1, 10, 10, dtype="e")
print(v)

np.save("vector.npy", v, allow_pickle=False)
