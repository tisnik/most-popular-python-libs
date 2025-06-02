#!/usr/bin/env python3
# vim: set fileencoding=utf-8
#
# Knihovna XLSXWriter
#
# - vytvoření sešitu s několika vyplněnými buňkami
# - adresace buněk specifikací sloupce a řádku

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
# https://github.com/tisnik/most-popular-python-libs/blob/master/PySimpleGUI/04_alternative_addressing.py
#
# link to source in literate programming format:
# https://tisnik.github.io/most-popular-python-libs/PySimpleGUI/04_alternative_addressing.html

"""Vytvoření sešitu s několika vyplněnými buňkami."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook("example04.xlsx") as workbook:
    # vložení nového listu do sešitu
    worksheet = workbook.add_worksheet()

    # buňka s textem
    worksheet.write(0, 0, "www.root.cz")

    # buňky s numerickými hodnotami
    worksheet.write(1, 0, 6)
    worksheet.write(2, 0, 7)
    worksheet.write(2, 1, 8)

    # sešit bude uzavřen automaticky
