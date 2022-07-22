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

# rozměry matice
rows = 1000
columns = 1000

# vytvoření větší matice o zadaném tvaru
m0 = np.zeros((rows, columns), dtype="i")

# uložení matice do souboru ve standardním formátu
np.savez("matrix_uncompressed.npz", m0)

# uložení matice do souboru ve standardním zkomprimovaném formátu
np.savez_compressed("matrix_compressed.npz", m0)
