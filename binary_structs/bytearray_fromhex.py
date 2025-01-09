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

x = bytearray.fromhex("")
print(type(x))
print(x)

print()

y = bytearray.fromhex("00 0f 1f ff")
print(type(y))
print(y)

print()

z = bytearray.fromhex("000f1fff")
print(type(z))
print(z)
