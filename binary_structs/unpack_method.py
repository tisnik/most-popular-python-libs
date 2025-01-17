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

# uložení hodnoty bajtu do binární struktury
bytes = struct.pack("b", 42)
print("Serialized:  ", bytes.hex(" ", 1))

# přečtení binární struktury, která obsahuje jediný bajt
s = struct.Struct("b")
from_struct = s.unpack(bytes)

# vypsat přečtenou hodnotu
print("Deserialized:", from_struct)
print("Type:        ", type(from_struct))
