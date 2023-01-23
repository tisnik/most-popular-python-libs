#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import polars

# přečtení zdrojových dat
with polars.StringCache():
    df = polars.read_csv("hall_of_fame.csv")

    # seskupení podle názvu jazyka
    df2 = (
        df.groupby("Winner", maintain_order=True)
        .agg([polars.col("Year").len().alias("Zvítězil")])
        .sort("Zvítězil")
        .reverse()
        .head(5)
    )

    # zobrazíme výsledný datový rámec
    print(df2)
    print()
    print(df2.columns)
    print(df2.dtypes)
