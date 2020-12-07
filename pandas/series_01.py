#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

s = pandas.Series((1, 2, 3, 4, 5, 6))

print("Series:")
print(s)
print()

print("Index:")
print(s.index)
print()

print("Values:")
print(s.values)
print()
