"""Uložení obsahu vektoru do textového souboru se specifikací oddělovače."""

import numpy as np

# vektor obsahující celočíselné 8bitové hodnoty (byte)
v = np.linspace(1, 10, 10, dtype="b")
print(v)

v.tofile("vector1.txt", sep=",")
