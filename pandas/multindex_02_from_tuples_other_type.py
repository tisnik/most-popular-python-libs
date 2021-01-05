#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

sequence1 = range(10)
sequence2 = ["foo", "bar", "baz", "foo", "bar", "baz", "foo", "bar", "baz", "*"]

zipped = zip(sequence1, sequence2)

print("zipped sequences")
print(zipped)
print()

lst = list(list(x) for x in zipped)

print("converted to list")
print(lst)
print()

multiindex = pandas.MultiIndex.from_tuples(lst)

print("multiindex made from tuples")
print(multiindex)
print()
