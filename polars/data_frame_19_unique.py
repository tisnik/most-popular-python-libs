#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import polars

# přečtení zdrojových dat
df = polars.read_csv("hall_of_fame.csv")

# maximální počet zobrazených řádků
polars.Config.set_tbl_rows(100)

# seřadit a vytvořit nový datový rámec
df = df.unique(subset="Winner")

# zobrazíme datový rámec
print(df)
