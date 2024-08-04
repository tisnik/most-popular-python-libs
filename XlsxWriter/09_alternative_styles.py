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
# https://github.com/tisnik/most-popular-python-libs/blob/master/PySimpleGUI/09_alternative_styles.py
#
# link to source in literate programming format:
# https://tisnik.github.io/most-popular-python-libs/PySimpleGUI/09_alternative_styles.html

"""Vytvoření sešitu s delší tabulkou, nastavení stylů vybraných buněk."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook("example09.xlsx") as workbook:
    # vložení nového listu do sešitu
    worksheet = workbook.add_worksheet()

    # nastavení šířky sloupců
    worksheet.set_column("A:A", 8)
    worksheet.set_column("B:B", 14)
    worksheet.set_column("C:Z", 2)

    # definice nového stylu
    bold_style = workbook.add_format()
    bold_style.set_bold()
    bold_style.set_font_color("blue")

    # buňky s textem
    worksheet.write("A1", "x", bold_style)
    worksheet.write("B1", "1/x", bold_style)

    # buňky s numerickými hodnotami
    for x in range(1, 21):
        worksheet.write(x, 0, x)
        worksheet.write(x, 1, 1.0 / x)

    # sešit bude uzavřen automaticky
