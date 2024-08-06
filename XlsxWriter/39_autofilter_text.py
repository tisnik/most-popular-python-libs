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
# https://github.com/tisnik/most-popular-python-libs/blob/master/PySimpleGUI/39_autofilter_text.py
#
# link to source in literate programming format:
# https://tisnik.github.io/most-popular-python-libs/PySimpleGUI/39_autofilter_text.html

"""Automatické filtry."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook("example39.xlsx") as workbook:
    # vložení nového listu do sešitu
    worksheet = workbook.add_worksheet()

    # definice nového stylu
    bold_style = workbook.add_format()
    bold_style.set_bold()
    bold_style.set_font_color("blue")

    # definice dalšího nového stylu
    red_style = workbook.add_format()
    red_style.set_font_color("red")

    # definice formátu čísel
    numeric_format = workbook.add_format({"num_format": "0.0000"})

    # nastavení šířky sloupců a stylu
    worksheet.set_column("A:A", 8)
    worksheet.set_column("B:B", 14, numeric_format)
    worksheet.set_column("C:Z", 20)

    # styl pro první řádek
    worksheet.set_row(0, 20, bold_style)

    # buňky s textem
    worksheet.write_string("A1", "x")
    worksheet.write_string("B1", "1/x")
    worksheet.write_string("C1", "valid?")

    # buňky s numerickými hodnotami
    for x in range(1, 21):
        worksheet.write_number(x, 0, x)
        worksheet.write_number(x, 1, 1.0 / x)
        msg = "yes" if x % 2 == 0 else "no"
        worksheet.write_string(x, 2, msg)

    # nastavení automatického filtru
    worksheet.autofilter("A1:C21")

    # formát s podmínkou
    conditional_format = {
        "type": "cell",
        "criteria": ">=",
        "value": 0.2,
        "format": red_style,
    }

    # nastavení podmíněného formátu u druhého sloupce hodnot
    worksheet.conditional_format("B2:B21", conditional_format)

    # sešit bude uzavřen automaticky
