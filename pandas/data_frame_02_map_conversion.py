#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")

# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)

# převod na skutečný poměr <0, 1>
df["Ratings as ratio"] = df["Ratings"].map(lambda x: x / 100.0)

# datový rámec zobrazíme
print(df)
print()

# podrobnější informace o datovém rámci
print(df.dtypes)
print()

# více podrobnějších informací o datovém rámci
print(df.info())
print()
