"""Uložení obsahu vektoru do binárního souboru."""

import numpy as np

# vektor obsahující hodnoty s plovoucí řádovou čárkou
# s dvojitou přesností (double)
v = np.linspace(1, 10, 10, dtype="d")
print(v)

v.tofile("vector8.bin")
