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

from tabulate import tabulate, _table_formats as table_styles
import pandas

# přečtení zdrojových dat
df = pandas.read_csv("tiobe.tsv", sep="\t")

# specifikace indexu - má se získat ze sloupce Language
df.set_index("Language", inplace=True)

# zobrazit tabulku ve všech podporovaných formátech
for table_style in table_styles:
    # oddělovač
    print()
    print("*" * 40)
    print("* {:^36s} *".format(table_style))
    print("*" * 40)
    print()
    # datový rámec zobrazíme s vybraným stylem
    print(tabulate(df, headers="keys", tablefmt=table_style))
