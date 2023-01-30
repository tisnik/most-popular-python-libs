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
df1 = polars.read_csv("tiobeA.tsv", sep="\t")
df2 = polars.read_csv("tiobeB.tsv", sep="\t")

# datové rámce zobrazíme
print(df1)
print()
print(df2)
print()

# spojení obou datových rámců
merged = df2.join(df1, on="Language", how="anti")

# výpis výsledku
print(merged)
