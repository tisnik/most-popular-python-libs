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
#
# link to source:
# https://github.com/tisnik/most-popular-python-libs/blob/master/PySimpleGUI/27_merged_cells.py
# 
# link to source in literate programming format:
# https://tisnik.github.io/most-popular-python-libs/PySimpleGUI/27_merged_cells.html

"""Vytvoření sešitu se sloučenými buňkami."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook("example27.xlsx") as workbook:
    # vložení nového listu do sešitu
    worksheet = workbook.add_worksheet()

    # první formát použitý pro zvýraznění sloučené buňky
    format1 = workbook.add_format(
        {
            "bold": 1,
            "border": 1,
            "align": "center",
            "valign": "vcenter",
            "fg_color": "#ff8080",
        }
    )

    # druhý formát použitý pro zvýraznění sloučené buňky
    format2 = workbook.add_format(
        {
            "bold": 1,
            "border": 1,
            "align": "center",
            "valign": "vcenter",
            "fg_color": "#80ff80",
        }
    )

    # sloučená buňka
    worksheet.merge_range("B2:D2", "Sloučená buňka", format1)

    # sloučená buňka
    worksheet.merge_range("F2:F4", "Sloučená\nbuňka", format2)

    # sešit bude uzavřen automaticky
