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
df = polars.read_csv("timestamps.csv", parse_dates=True)

# zobrazíme datový rámec
print(df)
print()

# podrobnější informace o datovém rámci
print("Column types")
print(df.dtypes)
print()
