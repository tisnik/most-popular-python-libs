#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")

# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)

# agregace výsledků
results = df["Ratings"].agg(["min", "max", "sum", "mean"])

# tisk vypočtených výsledků
print("Results")
print(results)
