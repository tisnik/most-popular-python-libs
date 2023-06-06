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
import numpy as np

# přečtení zdrojových dat s jejich konverzí do datového rámce
df = pandas.read_csv("denni_kurz2.txt", sep="|", skiprows=0)

# převod číselných hodnot
df["kurz"] = pandas.to_numeric(df["kurz"].str.replace(",", "."), errors="coerce")

# datový rámec zobrazíme
print(df)
print()

# rozdělení do skupin podle data
gb = df.groupby(["kód"])

# výpočet a zobrazení základní statistiky
print(gb["kurz"].agg([np.min, np.max, np.mean, np.std]))
