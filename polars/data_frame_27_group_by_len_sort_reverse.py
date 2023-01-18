#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2023  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import polars

# přečtení zdrojových dat
df = polars.read_csv("hall_of_fame.csv")

# maximální počet zobrazených řádků
polars.Config.set_tbl_rows(100)

# seskupení podle názvu jazyka
df = (
    df.groupby("Winner", maintain_order=True)
    .agg([polars.col("Year").len()])
    .sort("Year")
    .reverse()
)

# zobrazíme datový rámec
print(df)
