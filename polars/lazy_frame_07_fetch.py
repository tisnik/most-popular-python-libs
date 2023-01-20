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
df = polars.scan_csv("hall_of_fame.csv")

# zobrazíme plán pro líně načtený datový rámec
print(df.describe_plan())
print()

# aplikace operace na líný datový rámec
df2 = df.sort("Winner").reverse()

# převod vybraných prvků na běžný datový rámec
df3 = df2.fetch(5)

# zobrazíme plán pro druhý líny datový rámec
print(df2.describe_plan())
print()

# zobrazíme běžný (výsledný) datový rámec
print(df3)
print()
print(df3.columns)
print(df3.dtypes)
