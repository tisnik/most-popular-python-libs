#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from tabulate import tabulate
import pandas

# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")

# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)

# jména stylů
table_styles = (
    "plain",
    "simple",
    "github",
    "grid",
    "fancy_grid",
    "pipe",
    "orgtbl",
    "jira",
    "presto",
    "pretty",
    "psql",
    "rst",
    "mediawiki",
    "moinmoin",
    "youtrack",
    "html",
    "latex",
    "latex_raw",
    "latex_booktabs",
    "textile",
    "tsv",
)

for table_style in table_styles:
    # oddělovač
    print()
    print("*" * 40)
    print("* {:^36s} *".format(table_style))
    print("*" * 40)
    print()
    # datový rámec zobrazíme s vybraným stylem
    print(tabulate(df, headers="keys", tablefmt=table_style))
