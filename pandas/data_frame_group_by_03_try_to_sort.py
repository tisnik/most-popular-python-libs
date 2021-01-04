#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

# přečtení zdrojových dat
df = pandas.read_csv("hall_of_fame.tsv", sep="\t")

# specifikace indexu - má se získat ze sloupce Year
df.set_index("Year", inplace=True)

# datový rámec zobrazíme
print(df)
print()

# rozdělení do skupin
gb = df.groupby(["Winner"])

# agregace výsledků
result = gb[["Winner"]].count()

# pokusíme se o seřazení hodnot podle jediného sloupce
result.sort_values(by=["Winner"], inplace=True)

# zobrazení výsledků
print(result)
