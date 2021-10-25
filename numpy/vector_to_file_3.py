"""Uložení obsahu vektoru do binárního souboru."""

import numpy as np

# vektor obsahující celočíselné 8bitové hodnoty (byte)
v = np.linspace(1, 10, 10, dtype="b")
print(v)

v.tofile("vector3.bin")
