#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from array import array

from pympler.asizeof import asizeof

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
for i in range(1000):
    l1.append(i % 100)
    a1.append(i % 100)
    a2.append(i % 100)
    a3.append(i % 100)
    a4.append(i % 100)
    a5.append(i % 100)
    a6.append(i % 100)
    a7.append(i % 100)

# výpis skutečných velikostí
print("List:             ", asizeof(l1))
print("Array of bytes:   ", asizeof(a1))
print("Array of shorts:  ", asizeof(a2))
print("Array of ints:    ", asizeof(a3))
print("Array of longs:   ", asizeof(a4))
print("Array of quads:   ", asizeof(a5))
print("Array of floats:  ", asizeof(a6))
print("Array of doubles: ", asizeof(a7))
