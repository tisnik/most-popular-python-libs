#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Čtení hodnot prvků uložených v polích."""

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
l1 = []
a1 = array("B")
a2 = array("H")
a3 = array("I")
a4 = array("L")
a5 = array("Q")
a6 = array("f")
a7 = array("d")

# naplnit daty
for i in range(100):
    l1.append(i)
    a1.append(i)
    a2.append(i)
    a3.append(i)
    a4.append(i)
    a5.append(i)
    a6.append(i)
    a7.append(i)


def print_all_items(name, struct):
    """Vytištění všech prvků uložených ve struktuře."""
    print(name)
    for item in struct:
        print(item, end=" ")
    print("\n")


print_all_items("List:", l1)
print_all_items("Array of bytes:", a1)
print_all_items("Array of shorts:", a2)
print_all_items("Array of ints:", a3)
print_all_items("Array of longs:", a4)
print_all_items("Array of quads:", a5)
print_all_items("Array of floats:", a6)
print_all_items("Array of doubles:", a7)
