#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Reading text file that contains columns with fixed width."""

import pandas

# separator/delimiter specification
df = pandas.read_fwf("tiobe.txt", widths=(20, 20, 20, 20, 20, 20))

print("Data frame")
print("---------------------------")
print(df)
print()

print("Column types")
print("---------------------------")
print(df.dtypes)
