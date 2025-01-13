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

x = bytes(b"The quick brown fox jumps over the lazy dog")
print(x.hex())
print(x.hex(" "))
print(x.hex(" ", 2))
print(x.hex(" ", 4))
