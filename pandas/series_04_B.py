#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

s = pandas.Series(range(1, 3), ('a', 'b', 'c', 'd', 'e', 'f', 'g'))


print("Series:")
print(s)
print()

print("Index:")
print(s.index)
print()

print("Values:")
print(s.values)
print()
