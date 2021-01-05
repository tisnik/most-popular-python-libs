#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

sequence1 = range(10)
sequence2 = ("foo", "bar", "baz", "foo", "bar", "baz", "foo", "bar", "baz", "*")

zipped = zip(sequence1, sequence2)

print("zipped sequences")
print(zipped)
print()

tuples = tuple(zipped)

print("converted to tuples")
print(tuples)
print()

multiindex = pandas.MultiIndex.from_tuples(tuples)

print("multiindex made from tuples")
print(multiindex)
print()
