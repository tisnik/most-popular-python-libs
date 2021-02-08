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
print(s)
print()

# maskování hodnot
s.mask(s > 10, inplace=False)

# tisk výsledku
print("Masked (max)")
print(s)
print()

# maskování hodnot
s.mask(s < 2, inplace=False)

# tisk výsledku
print("Masked (min)")
print(s)
