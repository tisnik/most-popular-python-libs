#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Změna alokované paměti při postupném přidávání prvků do polí."""

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

from pympler.asizeof import asizeof

# prázdné struktury
l1 = []
a1 = array("B")
a2 = array("H")
a3 = array("I")
a4 = array("L")

# naplnit daty
for i in range(200):
    l1.append(i)
    a1.append(i%100)
    a2.append(i%100)
    a3.append(i)
    a4.append(i)

    # výpis skutečných velikostí
    print(i, asizeof(l1), asizeof(a1), asizeof(a2), asizeof(a3), asizeof(a4))
