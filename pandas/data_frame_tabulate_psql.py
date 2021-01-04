#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from tabulate import tabulate
import pandas

# přečtení zdrojových dat
df = pandas.read_csv("hall_of_fame.tsv", sep="\t")

# specifikace indexu - má se získat ze sloupce Year
df.set_index("Year", inplace=True)

# datový rámec zobrazíme
print(tabulate(df, headers="keys", tablefmt="psql"))
print()

# rozdělení do skupin
gb = df.groupby(["Winner"])

# agregace výsledků
result = gb[["Winner"]].count()

# přejmenování sloupce
result.rename(columns={"Winner": "Language"}, inplace=True)

# seřazení výsledků
result.sort_values(by=["Language"], inplace=True, ascending=False)

# zobrazení výsledků
print(tabulate(result, headers="keys", tablefmt="psql"))
