#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import polars

# maximální počet zobrazených řádků
polars.Config.set_tbl_rows(100)

# přečtení zdrojových dat
df1 = polars.read_csv("tiobeE.tsv", sep="\t")
df2 = polars.read_csv("tiobeF.tsv", sep="\t")

# datové rámce zobrazíme
print(df1)
print()
print(df2)
print()

# spojení obou datových rámců
concatenated = polars.concat([df1, df2], how="horizontal")

# výpis výsledku
print(concatenated)
