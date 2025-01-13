#
#  (C) Copyright 2025  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

x = bytes(10)
print(type(x))
print(x)

print()

y = bytes((1, 2, 3, 254, 255))
print(type(y))
print(y)

print()

z = bytes()
print(type(z))
print(z)
