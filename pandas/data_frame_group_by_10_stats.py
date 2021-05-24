#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas
import numpy as np

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
