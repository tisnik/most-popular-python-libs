"""Načtení obsahu matice z binárního souboru se specifikací formátu."""

import numpy as np

# rozměry výsledné matice
rows = 500
columns = 5

# načtení prvků matice z binárního souboru a konstrukce matice
m = np.fromfile("matrix3.bin", dtype="i").reshape(rows, columns)

# výpis obsahu právě zkonstruované matice
print(m)
