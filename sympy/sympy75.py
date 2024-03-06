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

a = sp.MatrixSymbol("A", 3, 4)
b = sp.MatrixSymbol("B", 4, 3)

sp.pprint(sp.Matrix(a))

print()

sp.pprint(sp.Matrix(b))

print()

c = a * b
sp.pprint(sp.Matrix(c))
