#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import pandas

# přečtení zdrojových dat
df1 = pandas.read_csv("tiobeA.tsv", sep="\t")
df2 = pandas.read_csv("tiobeB.tsv", sep="\t")

# datové rámce zobrazíme
print(df1)
print()
print(df2)
print()

# spojení obou datových rámců
merged = pandas.merge(df1, df2)

# výpis výsledku
print(merged)
