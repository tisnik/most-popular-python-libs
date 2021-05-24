#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

sequence1 = range(1, 6)
sequence2 = ("foo", "bar", "baz")

sequences = (sequence1, sequence2)

print("sequences")
print(sequences)
print()

multiindex = pandas.MultiIndex.from_product(sequences, names=["first", "second"])

print("multiindex made from tuples")
print(multiindex)
print()
