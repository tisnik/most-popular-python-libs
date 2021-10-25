"""Uložení obsahu vektoru do binárního souboru."""

import numpy as np

# vektor obsahující celočíselné 64bitové hodnoty (long integer)
v = np.linspace(1, 10, 10, dtype="l")
print(v)

v.tofile("vector6.bin")
