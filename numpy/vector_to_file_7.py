"""Uložení obsahu vektoru do binárního souboru."""

import numpy as np

# vektor obsahující hodnoty s plovoucí řádovou čárkou
# s jednoduchou přesností (float, single)
v = np.linspace(1, 10, 10, dtype="f")
print(v)

v.tofile("vector7.bin")
