#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import polars

# přečtení zdrojových dat
df = polars.read_csv("hall_of_fame.csv")

# převod na líný datový rámec
df2 = df.lazy()

# zobrazíme načtený datový rámec
print(df)
print()

# následně zobrazíme líný datový rámec
print(df2)
print()
