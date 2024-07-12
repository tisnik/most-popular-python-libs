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
# https://github.com/tisnik/most-popular-python-libs/blob/master/PySimpleGUI/22_show_comments.py
# 
# link to source in literate programming format:
# https://tisnik.github.io/most-popular-python-libs/PySimpleGUI/22_show_comments.html

"""Tabulka s komentáři přirazenými k vybraným buňkám."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook("example22.xlsx") as workbook:
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
    worksheet.set_column("A:A", 8, red_style)
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
        worksheet.write_comment(x, 1, "Výsledek výrazu 1/{}".format(x))

    # komentáře by měly být zobrazeny ihned po otevření sešitu
    worksheet.show_comments()

    # sešit bude uzavřen automaticky
