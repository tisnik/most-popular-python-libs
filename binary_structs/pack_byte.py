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

import struct

bytes1 = struct.pack("b", 42)
print(type(bytes1))
print(bytes1.hex(" ", 1))

print()

bytes2 = struct.pack("B", 42)
print(type(bytes2))
print(bytes2.hex(" ", 1))
