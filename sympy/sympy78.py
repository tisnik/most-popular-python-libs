#
#  (C) Copyright 2023  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import sympy as sp

a = sp.MatrixSymbol("A", 2, 2)
b = sp.MatrixSymbol("B", 2, 2)

c = a * b

sp.pprint(sp.Matrix(c))

print()

sp.pprint(sp.Matrix(c.I))
