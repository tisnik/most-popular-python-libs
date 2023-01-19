#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import polars

# líné přečtení zdrojových dat
df = polars.scan_csv("hall_of_fame.csv")

# zobrazíme líně načtený datový rámec
print(df)
print()

# převod na běžný datový rámec
df2 = df.collect()

# zobrazíme běžný (výsledný) datový rámec
print(df2)
print()
print(df2.columns)
print(df2.dtypes)
