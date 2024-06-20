#!/usr/bin/env python3
# vim: set fileencoding=utf-8

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

# naplnit daty
for i in range(100):
    a1.append(i)
    a2.append(i)
    a3.append(i)
    a4.append(i)
    a5.append(i)
    a6.append(i)
    a7.append(i)


def export_to_file(filename, struct):
    """Export celé struktury do souboru."""
    with open(filename, "wb") as f:
        struct.tofile(f)


export_to_file("bytes.bin", a1)
export_to_file("shorts.bin", a2)
export_to_file("ints.bin", a3)
export_to_file("longs.bin", a4)
export_to_file("quads.bin", a5)
export_to_file("floats.bin", a6)
export_to_file("doubles.bin", a7)
