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
df = pandas.read_csv("tiobe.tsv", sep="\t")

# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)

# pro jistotu si datový rámec zobrazíme
print(df)
print()

# konstrukce datové struktury Series (datové řady) z datového rámce
s = pandas.Series(df["Ratings"])

# tisk obsahu původní datové řady
print(s)
print()

# maskování hodnot
s.mask(s > 10, inplace=True)

# tisk výsledku
print("Masked (max)")
print(s)
print()

# maskování hodnot
s.mask(s < 2, inplace=True)

# tisk výsledku
print("Masked (min)")
print(s)
