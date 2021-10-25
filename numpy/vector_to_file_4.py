"""Uložení obsahu vektoru do binárního souboru."""

import numpy as np

# vektor obsahující celočíselné 16bitové hodnoty (half integer)
v = np.linspace(1, 10, 10, dtype="h")
print(v)

v.tofile("vector4.bin")
