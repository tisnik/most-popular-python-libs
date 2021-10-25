"""Uložení obsahu vektoru do binárního souboru."""

import numpy as np

# vektor obsahující celočíselné 32bitové hodnoty (integer)
v = np.linspace(1, 10, 10, dtype="i")
print(v)

v.tofile("vector5.bin")
