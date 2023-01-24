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

# líné přečtení zdrojových dat
df1 = polars.scan_csv("hall_of_fame.csv")

# seřazení podle zvoleného sloupce
df2 = df1.sort("Year")

# seřazení podle zvoleného sloupce
df3 = df1.sort("Year", reverse=True)

# seskupení podle názvu jazyka
df4 = (
    df2.groupby("Winner", maintain_order=True)
    .agg([polars.col("Year").len().alias("Zvítězil")])
    .sort("Zvítězil")
)

# otočení prvků + získání pěti výsledků
df5 = df4.reverse().head(5)

# spojení několika datových rámců - spojení plánů
df6 = polars.concat([df2, df3, df4, df5], how="vertical")

# zobrazíme plány pro všechny líné datové rámce
print("df1")
print(df1.describe_plan())
print()

print("df2")
print(df2.describe_plan())
print()

print("df3")
print(df3.describe_plan())
print()

print("df4")
print(df4.describe_plan())
print()

print("df5")
print(df5.describe_plan())
print()

print("df6")
print(df6.describe_plan())
print()
