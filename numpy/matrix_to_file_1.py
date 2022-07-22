"""Uložení obsahu matice do textového souboru se specifikací oddělovače."""

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

# matice obsahující celočíselné 8bitové hodnoty (byte)
m = np.linspace(1, 12, 12, dtype="b").reshape(3, 4)
print(m)

m.tofile("matrix1.txt", sep=",")
