#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Reading TSV file that contains column with various values."""

import pandas

df = pandas.read_csv("tiobe.tsv")

print("Data frame")
print("---------------------------")
print(df)
print()

print("Column types")
print("---------------------------")
print(df.dtypes)
