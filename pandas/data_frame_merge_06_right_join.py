#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

# přečtení zdrojových dat
df1 = pandas.read_csv("tiobeA.tsv", sep="\t")
df2 = pandas.read_csv("tiobeB.tsv", sep="\t")

# specifikace indexu - má se získat ze sloupce Language
df1.set_index("Language", inplace=True)
df2.set_index("Language", inplace=True)

# datové rámce zobrazíme
print(df1)
print()
print(df2)
print()

# spojení obou datových rámců
merged = pandas.merge(df1, df2, left_index=True, right_index=True,
                      how="right",
                      on=["Change", "Ratings", "Changep"])

# výpis výsledku
print(merged)
