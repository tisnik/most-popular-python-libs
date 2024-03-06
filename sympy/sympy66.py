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

a1 = sp.Array(range(16))
sp.pprint(a1)
print(a1.rank())
print(a1.shape)

print()

a2 = a1.reshape(2, 2, 2, 2)
sp.pprint(a2)
print(a2.rank())
print(a2.shape)
