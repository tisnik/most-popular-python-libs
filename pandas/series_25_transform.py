#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")

# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)

# pro jistotu si datový rámec zobrazíme
print(df)
print()

# konstrukce datové struktury Series (datové řady) z datového rámce
s = pandas.Series(df["Ratings"])

# tisk obsahu původní datové řady
print("In percents")
print(s)
print()

# převod na skutečný poměr <0, 1>
s2 = s.transform(lambda x: x/100.0)

# tisk obsahu nové datové řady
print("As ratios")
print(s2)
