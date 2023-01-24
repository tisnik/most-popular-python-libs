#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import polars

# maximální počet zobrazených řádků
polars.Config.set_tbl_rows(100)

# přečtení zdrojových dat
df1 = polars.read_csv("tiobeA.tsv", sep="\t")
df2 = polars.read_csv("tiobeB.tsv", sep="\t")

# datové rámce zobrazíme
print(df1)
print()
print(df2)
print()

# spojení obou datových rámců
merged = df1.join(df2, on="Language", how="cross")

# výpis výsledku
print(merged)
