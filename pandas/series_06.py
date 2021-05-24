#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

input_data = {
        "f": 6,
        "e": 5,
        "d": 4,
        "c": 3,
        "b": 2,
        "a": 1,
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
