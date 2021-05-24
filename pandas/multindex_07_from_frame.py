#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")

del df["Sep 2020"]
del df["Ratings"]
del df["Change"]
del df["Changep"]

# datový rámec zobrazíme
print(df)
print()

multiindex = pandas.MultiIndex.from_frame(df)

print("multiindex made from data frame")
print(multiindex)
print()
