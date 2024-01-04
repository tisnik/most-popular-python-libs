#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from pympler.asizeof import asizeof
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

# výpis skutečných velikostí
print("List:             ", asizeof(l1))
print("Array of bytes:   ", asizeof(a1))
print("Array of shorts:  ", asizeof(a2))
print("Array of ints:    ", asizeof(a3))
print("Array of longs:   ", asizeof(a4))
print("Array of quads:   ", asizeof(a5))
print("Array of floats:  ", asizeof(a6))
print("Array of doubles: ", asizeof(a7))
