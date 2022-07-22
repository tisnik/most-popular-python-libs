"""Načtení obsahu matice z binárního souboru se specifikací formátu."""

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

# rozměry výsledné matice
rows = 500
columns = 5

# načtení prvků matice z binárního souboru a konstrukce matice
m = np.fromfile("matrix3.bin", dtype="i").reshape(rows, columns)

# výpis obsahu právě zkonstruované matice
print(m)
