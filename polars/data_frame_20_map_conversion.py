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
