#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import polars

# maximální počet zobrazených řádků
polars.Config.set_tbl_rows(100)

# přečtení zdrojových dat
df = polars.read_csv("tiobe.tsv", sep="\t")

# převod na skutečný poměr <0, 1>
df2 = df.with_column(
    polars.col("Ratings").map(lambda x: x / 100.0).alias("Ratings as ratio")
)

# datový rámec zobrazíme
print(df)
print()

# datový rámec zobrazíme
print(df2)
print()
