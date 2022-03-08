"""Načtení obsahu datového rámce z binárního souboru se specifikací formátu."""

import numpy as np
import pandas as pd

dt = np.dtype(
    [
        ("i", "<u4"),
        ("x", "<f4"),
        ("type", "S4"),
    ]
)

np_data = np.fromfile("binary_df_2.bin", dtype=dt)
print(np_data)
print(np_data.ndim)
print(np_data.dtype)

df = pd.DataFrame(np_data)
df["type"] = df["type"].str.decode("utf-8")

print(df)
print()
print(df.info())
print()
print(df.describe())
