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

# počet referencí na řetězec 'Test!'
print(sys.getrefcount(x))

# více referencí na řetězec
y = [x, "Test!"]

# nový počet referencí na řetězec 'Test!'
print(sys.getrefcount(x))

del y[1]

# nový počet referencí na řetězec 'Test!'
print(sys.getrefcount(x))

del y[0]

# nový počet referencí na řetězec 'Test!'
print(sys.getrefcount(x))

x = None

# nový počet referencí na řetězec 'Test!'
print(sys.getrefcount("Test!"))
