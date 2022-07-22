"""Uložení obsahu matice do standardního binárního souboru."""

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

# rozměry matice
rows = 1000
columns = 5

# matice obsahující celočíselné hodnoty typu integer
m = np.linspace(1, rows * columns, rows * columns, dtype="i").reshape(rows, columns)

# tisk obsahu zkonstruované matice
print(m)

# uložení matice do souboru ve standardním formátu
np.save("matrix3.npy", m, allow_pickle=False)
