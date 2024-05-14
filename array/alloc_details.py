#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from array import array

from pympler.asizeof import asizeof

# prázdná struktura
a1 = array("B")

last_size = asizeof(a1)
last_index = 0

# naplnit daty
for i in range(1000):
    a1.append(i%100)
    size = asizeof(a1)
    if size != last_size:
        print(f"{i:5}  {size:5}  {size-last_size:+5}   {last_index:4}-{i:<4}")
        last_index = i
        last_size = size
