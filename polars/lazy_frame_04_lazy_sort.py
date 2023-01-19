#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import polars

# líné přečtení zdrojových dat
df = polars.scan_csv("hall_of_fame.csv")

# zobrazíme líně načtený datový rámec
print(df)
print()

# aplikace operace na líný datový rámec
df2 = df.sort("Winner")

# převod na běžný datový rámec
df3 = df2.collect()

# zobrazíme druhý líny datový rámec
print(df2)
print()

# zobrazíme běžný (výsledný) datový rámec
print(df3)
print()
print(df3.columns)
print(df3.dtypes)
