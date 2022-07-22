"""Uložení obsahu vektoru do standardního binárního souboru."""

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

# vektor obsahující hodnoty s plovoucí řádovou čárkou
# s poloviční přesností (half)
v = np.linspace(1, 10, 10, dtype="e")
print(v)

np.save("vector.npy", v, allow_pickle=False)
