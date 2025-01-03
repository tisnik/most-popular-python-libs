#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Import celých polí ze souboru."""

#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from array import array

# prázdné struktury
a1 = array("B")
a2 = array("H")
a3 = array("I")
a4 = array("L")
a5 = array("Q")
a6 = array("f")
a7 = array("d")


def import_from_file(filename, struct):
    """Import celé struktury ze souboru."""
    with open(filename, "rb") as f:
        struct.fromfile(f, 100)
    return struct


print(import_from_file("bytes.bin", a1))
print(import_from_file("shorts.bin", a2))
print(import_from_file("ints.bin", a3))
print(import_from_file("longs.bin", a4))
print(import_from_file("quads.bin", a5))
print(import_from_file("floats.bin", a6))
print(import_from_file("doubles.bin", a7))
