"""Uložení obsahu vektoru do binárního souboru."""

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

# vektor obsahující celočíselné 8bitové hodnoty (byte)
v = np.linspace(1, 10, 10, dtype="b")
print(v)

v.tofile("vector3.bin")
