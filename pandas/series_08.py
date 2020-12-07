#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

s = pandas.Series(range(1, 7), ('a', 'b', 'c', 'd', 'e', 'f'))

print("Series:")
print(s)
print()

print("Index:")
print(s.index)
print()

print("Values:")
print(s.values)
print()

s = s.reindex(['d', 'a', 'b', 'c', 'd', 'a', 'a', 'a'])

print("Reindexed:")
print()

print("Series:")
print(s)
print()

print("Index:")
print(s.index)
print()

print("Values:")
print(s.values)
print()

