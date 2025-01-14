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


def size_for_format(format):
    size = struct.calcsize(format)
    print(f"{format:>6}:{size}")


size_for_format("b")

print()

size_for_format("iBi")
size_for_format("=iBi")
size_for_format("@iBi")

print()

size_for_format("lBl")
size_for_format("=lBl")
size_for_format("@lBl")

print()

size_for_format("fBf")
size_for_format("=fBf")
size_for_format("@fBf")

print()

size_for_format("dBd")
size_for_format("=dBd")
size_for_format("@dBd")

print()

size_for_format("dBBd")
size_for_format("=dBBd")
size_for_format("@dBBd")

print()

size_for_format("dBBBd")
size_for_format("=dBBBd")
size_for_format("@dBBBd")
