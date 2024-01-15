#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from array import array

# prázdné struktury
a1 = array("B")
a2 = array("H")

# naplnit daty
for i in range(100):
    a1.append(i)
    a2.append(i)


with open("structured.bin", "wb") as f:
    f.write(b"HEADER\n")
    a1.tofile(f)
    f.write(b"\nsplitter\n")
    a2.tofile(f)
    f.write(b"END")
