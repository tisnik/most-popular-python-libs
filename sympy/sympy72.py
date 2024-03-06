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

a1 = sp.ImmutableSparseNDimArray(range(12))
a2 = a1.reshape(3, 4)

sp.pprint(a2)

print()

a3 = a2.transpose()
sp.pprint(a3)
