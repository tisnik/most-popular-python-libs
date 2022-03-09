#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

input_data = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
}

print("Input data:")
print(input_data)
print()

s = pandas.Series(input_data)

print("Series:")
print(s)
print()

print("Index:")
print(s.index)
print()

print("Values:")
print(s.values)
print()
