"""Zobrazení počtu referencí na řetězec."""

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

import sys

# více referencí na řetězec
x = "Test!"
print(x)

# počet referencí na řetězec 'Test!'
print(sys.getrefcount(x))

y = (x, x, x)
print(y)

# počet referencí na řetězec 'Test!'
print(sys.getrefcount(x))

z = (y, y)
print(z)

# počet referencí na řetězec 'Test!'
print(sys.getrefcount(x))

y = None
z = None

# nový počet referencí na řetězec 'Test!'
print(sys.getrefcount(x))
