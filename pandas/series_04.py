#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

s = pandas.Series(range(1, 10), ('a', 'b', 'c'))

print("Series:")
print(s)
print()

print("Index:")
print(s.index)
print()

print("Values:")
print(s.values)
print()
