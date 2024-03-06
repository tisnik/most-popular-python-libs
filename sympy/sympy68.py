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

a1 = sp.ImmutableSparseNDimArray([0] * 25)
a2 = a1.reshape(5, 5)

print(type(a2))
print()

sp.pprint(a2)
