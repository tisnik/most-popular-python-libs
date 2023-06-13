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

del df["Sep 2020"]
del df["Ratings"]
del df["Change"]
del df["Changep"]

# datový rámec zobrazíme
print(df)
print()

multiindex = pandas.MultiIndex.from_frame(df)

print("multiindex made from data frame")
print(multiindex)
print()
