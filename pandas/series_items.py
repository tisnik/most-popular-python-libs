#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")

# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)

# pro jistotu si datový rámec zobrazíme
print(df)

# konstrukce datové struktury Series z datového rámce
s = pandas.Series(df["Ratings"])

# tisk obsahu Series
print(s)

# iterace nad prvky rady
for index, value in s.items():
    print("Index: {:20}  Value: {:5.3}".format(index, value))
