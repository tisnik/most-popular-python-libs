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

m = np.fromfile("matrix2.bin", dtype="b").reshape(3, 4)

df = pd.DataFrame(m)

print(df)
print()
print(df.info())
print()
print(df.describe())
