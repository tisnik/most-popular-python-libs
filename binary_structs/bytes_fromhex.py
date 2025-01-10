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

x = bytes.fromhex("")
print(type(x))
print(x)

print()

y = bytes.fromhex("00 0f 1f ff")
print(type(y))
print(y)

print()

z = bytes.fromhex("000f1fff")
print(type(z))
print(z)
