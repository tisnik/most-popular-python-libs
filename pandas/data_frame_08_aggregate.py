#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas
import numpy as np

# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")

# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)

# agregace výsledků
results = df["Ratings"].agg([np.min, np.max, np.sum, np.mean])

# tisk vypočtených výsledků
print("Results")
print(results)
