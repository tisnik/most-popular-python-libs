#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import polars

# přečtení zdrojových dat
df = polars.read_csv("hall_of_fame_no_header.csv")

# zobrazíme datový rámec
print(df)
print()

# podrobnější informace o datovém rámci
print("Column types")
print(df.dtypes)
print()
