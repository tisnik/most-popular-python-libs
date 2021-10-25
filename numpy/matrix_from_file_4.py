"""Načtení obsahu matice z binárního souboru se specifikací formátu."""

import numpy as np

m = np.fromfile("matrix2.bin", dtype="b").reshape(3, 4)
print(m)
