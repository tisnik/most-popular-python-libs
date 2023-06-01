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

# formát hodnot ve sloupci
df["Ratings"] = df["Ratings"].transform("Rating is {:4.1f}%".format)

# datový rámec zobrazíme
print(df)
print()

# podrobnější informace o datovém rámci
print(df.dtypes)
print()

# více podrobnějších informací o datovém rámci
print(df.info())
print()
