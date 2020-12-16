#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")

# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)

# pro jistotu si datový rámec zobrazíme
print(df)

# konstrukce datové struktury Series (datové řady) z datového rámce
s = pandas.Series(df["Ratings"])

# tisk obsahu původní datové řady
print(s)
print()

# omezení hodnot
results = s.combine(10, min)

# tisk výsledku
print("Bound (max)")
print(results)

# omezení hodnot
results = results.combine(2, max)

# tisk výsledku
print("Bound (min)")
print(results)
