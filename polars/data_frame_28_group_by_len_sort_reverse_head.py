#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import polars

# přečtení zdrojových dat
df = polars.read_csv("hall_of_fame.csv")

# maximální počet zobrazených řádků
polars.Config.set_tbl_rows(100)

# seskupení podle názvu jazyka
df = df.groupby("Winner", maintain_order=True).agg([polars.col("Year").len().alias("Zvítězil")]). \
        sort("Zvítězil"). \
        reverse(). \
        head(5)

# zobrazíme datový rámec
print(df)
