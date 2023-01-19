#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import polars

# líné přečtení zdrojových dat
df = polars.scan_csv("hall_of_fame.csv")

# zobrazíme líně načtený datový rámec
print(df)
print()
