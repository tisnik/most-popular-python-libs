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

"""Podmíněné formátování, hodnoty mezi zadanými mezemi."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook("example33.xlsx") as workbook:
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
    worksheet.set_column("C:Z", 2)

    # styl pro první řádek
    worksheet.set_row(0, 20, bold_style)

    # buňky s textem
    worksheet.write_string("A1", "x")
    worksheet.write_string("B1", "1/x")

    # buňky s numerickými hodnotami
    for x in range(1, 21):
        worksheet.write_number(x, 0, x)
        worksheet.write_number(x, 1, 1.0 / x)

    # formát s podmínkou
    conditional_format = {
        "type": "cell",
        "criteria": "between",
        "minimum": 5,
        "maximum": 15,
        "format": red_style,
    }

    # nastavení podmíněného formátu u prvního sloupce hodnot
    worksheet.conditional_format(1, 0, 20, 0, conditional_format)

    # sešit bude uzavřen automaticky
