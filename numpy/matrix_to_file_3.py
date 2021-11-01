"""Uložení obsahu matice do binárního souboru."""

import numpy as np

# rozměry matice
rows = 500
columns = 5

# matice obsahující celočíselné hodnoty typu integer
m = np.linspace(1, rows*columns, rows*columns, dtype="i").reshape(rows, columns)

# tisk obsahu zkonstruované matice
print(m)

# uložení matice do souboru v čistém binárním formátu
m.tofile("matrix3.bin")
