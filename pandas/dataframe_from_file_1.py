"""Načtení obsahu datového rámce z binárního souboru se specifikací formátu."""

import numpy as np
import pandas as pd

m = np.fromfile("matrix2.bin", dtype="b").reshape(3, 4)

df = pd.DataFrame(m)

print(df)
print()
print(df.info())
print()
print(df.describe())
