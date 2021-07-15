"""Cyklické reference na různé hodnoty."""

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
import pprint

x = {}
y = {}

pprint.pprint(x)
pprint.pprint(y)
print(sys.getrefcount(x))
print(sys.getrefcount(y))
print()

x["1"] = y

pprint.pprint(x)
pprint.pprint(y)
print(sys.getrefcount(x))
print(sys.getrefcount(y))
print()

y["2"] = x

pprint.pprint(x)
pprint.pprint(y)
print(sys.getrefcount(x))
print(sys.getrefcount(y))
print()

del x["1"]

pprint.pprint(x)
pprint.pprint(y)
print(sys.getrefcount(x))
print(sys.getrefcount(y))
print()

del y["2"]

pprint.pprint(x)
pprint.pprint(y)
print(sys.getrefcount(x))
print(sys.getrefcount(y))
print()
