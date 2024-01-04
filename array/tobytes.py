#!/usr/bin/env python3
# vim: set fileencoding=utf-8

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
for i in range(10):
    a1.append(i)
    a2.append(i)
    a3.append(i)
    a4.append(i)
    a5.append(i)
    a6.append(i)
    a7.append(i)


def print_all_items_as_hex(name, struct):
    print(name)
    print(struct.tobytes().hex(" "))
    print()


print_all_items_as_hex("Array of bytes:", a1)
print_all_items_as_hex("Array of shorts:", a2)
print_all_items_as_hex("Array of ints:", a3)
print_all_items_as_hex("Array of longs:", a4)
print_all_items_as_hex("Array of quads:", a5)
print_all_items_as_hex("Array of floats:", a6)
print_all_items_as_hex("Array of doubles:", a7)
