#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas
import numpy as np

sequence2 = ("foo", "bar", "baz", "foo", "bar", "baz", "foo", "bar", "baz", "*")

s = pandas.Series(np.random.randn(10), index=sequence2)
print(s)
print()

print(s["foo"])
print()

print(s["bar"])
print()

print(s["baz"])
print()

print(s["*"])
print()

print(s["other"])
print()
