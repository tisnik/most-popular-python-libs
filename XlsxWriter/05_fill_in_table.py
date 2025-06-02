#!/usr/bin/env python3
# vim: set fileencoding=utf-8
#
# Knihovna XLSXWriter
#
# - vytvoření sešitu s delší tabulkou

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
#
# link to source:
# https://github.com/tisnik/most-popular-python-libs/blob/master/PySimpleGUI/05_fill_in_table.py
#
# link to source in literate programming format:
# https://tisnik.github.io/most-popular-python-libs/PySimpleGUI/05_fill_in_table.html

"""Vytvoření sešitu s delší tabulkou."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook("example05.xlsx") as workbook:
    # vložení nového listu do sešitu
    worksheet = workbook.add_worksheet()

    # buňky s textem
    worksheet.write("A1", "x")
    worksheet.write("B1", "1/x")

    # buňky s numerickými hodnotami
    for x in range(1, 21):
        worksheet.write(x, 0, x)
        worksheet.write(x, 1, 1.0 / x)

    # sešit bude uzavřen automaticky
