"""Načtení obsahu datového rámce z binárního souboru se specifikací formátu."""

#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import numpy as np
import pandas as pd

dt = np.dtype([("i", "u4"), ("x", "f4")])

np_data = np.fromfile("binary_df_1.bin", dtype=dt)
print(np_data)
print(np_data.ndim)
print(np_data.dtype)

df = pd.DataFrame(np_data)

print(df)
print()
print(df.info())
print()
print(df.describe())
