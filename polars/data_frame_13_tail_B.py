#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import polars

# přečtení zdrojových dat
df = polars.read_csv("hall_of_fame.csv")

# zobrazíme datový rámec
print(df.tail(30))
