"""Uložení obsahu vektoru do binárního souboru."""

import numpy as np

# vektor obsahující hodnoty s plovoucí řádovou čárkou
# s poloviční přesností (half)
v = np.linspace(1, 10, 10, dtype="e")
print(v)

v.tofile("vector9.bin")
