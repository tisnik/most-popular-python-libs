"""Uložení více matic do standardního binárního souboru."""

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

# rozměry první matice
rows1 = 10
columns1 = 10

# rozměry druhé matice
rows2 = 100
columns2 = 1

# rozměry třetí matice
rows3 = 1
columns3 = 100

# tři matice obsahující celočíselné hodnoty různých typů
m1 = np.linspace(1, rows1 * columns1, rows1 * columns1, dtype="b").reshape(
    rows1, columns1
)
m2 = np.linspace(1, rows2 * columns2, rows2 * columns2, dtype="i").reshape(
    rows2, columns2
)
m3 = np.linspace(1, rows3 * columns3, rows3 * columns3, dtype="f").reshape(
    rows3, columns3
)

# uložení matic do souboru ve standardním formátu
np.savez("matrix.npz", first=m1, second=m2, third=m3)
