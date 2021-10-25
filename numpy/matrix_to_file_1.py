"""Uložení obsahu matice do textového souboru se specifikací oddělovače."""

import numpy as np

# matice obsahující celočíselné 8bitové hodnoty (byte)
m = np.linspace(1, 12, 12, dtype="b").reshape(3, 4)
print(m)

m.tofile("matrix1.txt", sep=",")
