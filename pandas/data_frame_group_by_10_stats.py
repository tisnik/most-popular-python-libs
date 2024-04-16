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

import numpy as np
import pandas

# přečtení zdrojových dat s jejich konverzí do datového rámce
df = pandas.read_csv("git_log.txt", sep="|")

# datový rámec zobrazíme
print(df)
print()

# rozdělení do skupin podle data, autora i podle obou sloupců
gb1 = df.groupby(["Date"])
gb2 = df.groupby(["Author"])
gb3 = df.groupby(["Date", "Author"])

# zobrazení velikosti záznamů rozdělených do skupin
print(gb1.agg(np.size))
print(gb2.agg(np.size))
print(gb3.agg(np.size))
