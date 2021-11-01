"""Načtení obsahu matice z binárního souboru se specifikací formátu a offsetu."""

import numpy as np

# rozměry výsledné matice
rows = 250
columns = 5

# první řádek matice načtený z binárního souboru
first_row = 250

# platformově nezávislé získání počtu bajtů pro každý prvek typu integer
item_size = np.dtype("i").itemsize

# výpočet offsetu při čtení řádků od first_row z binárního souboru
offset = first_row * columns * item_size

print("offset=", offset, "bytes")
print()

# načtení prvků matice z binárního souboru a konstrukce matice
m = np.fromfile("matrix3.bin", dtype="i", offset=offset).reshape(rows, columns)

# výpis obsahu právě zkonstruované matice
print(m)
