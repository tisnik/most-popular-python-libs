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
df = pandas.read_csv("hall_of_fame.tsv", sep="\t")

# specifikace indexu - má se získat ze sloupce Year
df.set_index("Year", inplace=True)

# datový rámec zobrazíme
print(df)
print()

# rozdělení do skupin
gb = df.groupby(["Winner"])

# agregace výsledků
result = gb[["Winner"]].count()

# přejmenování sloupce
result.rename(columns={"Winner": "Language"}, inplace=True)

# seřazení výsledků v opačném pořadí (od nejlepšího)
result.sort_values(by=["Language"], inplace=True, ascending=False)

# zobrazení výsledků
print(result)
