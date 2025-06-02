#!/usr/bin/env python3
# vim: set fileencoding=utf-8
#
# Knihovna XLSXWriter
#
# - vytvoření sešitu s několika vyplněnými buňkami
# - adresace buněk stylem A1

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
# https://github.com/tisnik/most-popular-python-libs/blob/master/PySimpleGUI/03_simple_data.py
#
# link to source in literate programming format:
# https://tisnik.github.io/most-popular-python-libs/PySimpleGUI/03_simple_data.html

"""Vytvoření sešitu s několika vyplněnými buňkami."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook("example03.xlsx") as workbook:
    # vložení nového listu do sešitu
    worksheet = workbook.add_worksheet()

    # buňka s textem
    worksheet.write("A1", "www.root.cz")

    # buňky s numerickými hodnotami
    worksheet.write("A2", 6)
    worksheet.write("A3", 7)
    worksheet.write("B3", 8)

    # sešit bude uzavřen automaticky
