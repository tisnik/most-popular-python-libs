"""Reference na různé hodnoty."""

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

x = "foobar"
y = 0
z = True
w = None
lst = []

print(sys.getrefcount("foo"))
print(sys.getrefcount("foobar"))

print(sys.getrefcount(x))
print(sys.getrefcount(y))
print(sys.getrefcount(z))
print(sys.getrefcount(w))
print(sys.getrefcount(lst))
print(sys.getrefcount([]))
