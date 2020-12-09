#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import numpy as np
import pandas
import matplotlib.pyplot as plt

# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")

# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)

# pro jistotu si datový rámec zobrazíme
print(df)

# konstrukce datové struktury Series z datového rámce
s = pandas.Series(df["Ratings"])

# tisk obsahu Series
print(s)

# vytvoření grafu
s.plot.pie()

# uložení grafu
plt.savefig("series_plot_06.png")

# vykreslení grafu
plt.show()
