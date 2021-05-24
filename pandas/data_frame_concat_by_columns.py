#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

# přečtení zdrojových dat
df1 = pandas.read_csv("tiobeE.tsv", sep="\t")
df2 = pandas.read_csv("tiobeF.tsv", sep="\t")

# specifikace indexu - má se získat ze sloupce Language
df1.set_index("Language", inplace=True)
df2.set_index("Language", inplace=True)

# datové rámce zobrazíme
print(df1)
print()
print(df2)
print()

# spojení obou datových rámců
concatenated = pandas.concat([df1, df2], axis=1)

# výpis výsledku
print(concatenated)
