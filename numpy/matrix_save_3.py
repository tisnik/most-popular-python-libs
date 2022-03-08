"""Uložení obsahu matice do standardního binárního souboru."""

import numpy as np

# rozměry matice
rows = 1000
columns = 5

# matice obsahující celočíselné hodnoty typu integer
m = np.linspace(1, rows * columns, rows * columns, dtype="i").reshape(rows, columns)

# tisk obsahu zkonstruované matice
print(m)

# uložení matice do souboru ve standardním formátu
np.save("matrix3.npy", m, allow_pickle=False)
