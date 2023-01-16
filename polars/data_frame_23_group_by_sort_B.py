#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import polars

# přečtení zdrojových dat
df = polars.read_csv("hall_of_fame.csv")

# maximální počet zobrazených řádků
polars.Config.set_tbl_rows(100)

# seskupení podle názvu jazyka
df1 = df.groupby("Winner", maintain_order=True).agg([polars.col("Year")])
df2 = df.groupby("Winner", maintain_order=True).agg([polars.col("Year").sort()])

# výběr řádků s Pythonem, výběr dat ze sloupce Year a převod na seznam
print(df1[1]["Year"].to_list()[0])
print(df2[1]["Year"].to_list()[0])
