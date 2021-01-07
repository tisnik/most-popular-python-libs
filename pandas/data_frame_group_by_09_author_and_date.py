#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas
import pprint

# přečtení zdrojových dat s jejich konverzí do datového rámce
df = pandas.read_csv("git_log.txt", sep="|")

# datový rámec zobrazíme
print(df)
print()

# rozdělení do skupin podle data i autora (dvou sloupců)
gb = df.groupby(["Date", "Author"])

# zobrazení skupin vytvořených v rámci předchozího kroku
print("Group by date and author")
pprint.pprint(gb.groups)

# zobrazení počtu skupin
print()
print("Number of groups:", len(gb))
