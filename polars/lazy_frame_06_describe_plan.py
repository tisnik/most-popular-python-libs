#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import polars

# líné přečtení zdrojových dat
df = polars.scan_csv("hall_of_fame.csv")

# zobrazíme plán pro líně načtený datový rámec
print(df.describe_plan())
print(df.describe_optimized_plan())
print()

# aplikace operace na líný datový rámec
df2 = df.sort("Winner").reverse()

# převod na běžný datový rámec
df3 = df2.collect()

# zobrazíme plán pro druhý líny datový rámec
print(df2.describe_plan())
print(df2.describe_optimized_plan())
print()

# zobrazíme běžný (výsledný) datový rámec
print(df3)
print()
print(df3.columns)
print(df3.dtypes)
