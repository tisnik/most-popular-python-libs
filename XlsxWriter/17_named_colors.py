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

"""Vytvoření sešitu s delší tabulkou, nastavení barvy textu."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook("example17.xlsx") as workbook:
    # vložení nového listu do sešitu
    worksheet = workbook.add_worksheet()

    # nastavení šířky sloupců
    worksheet.set_column("A:A", 20)

    # barvy buněk
    colors = (
        "black",
        "blue",
        "brown",
        "cyan",
        "gray",
        "green",
        "lime",
        "magenta",
        "navy",
        "orange",
        "pink",
        "purple",
        "red",
        "silver",
        "white",
        "yellow",
    )

    # buňky s řetězci a různou barvou textu
    for x, color in enumerate(colors):
        style = workbook.add_format()
        style.set_font_color(color)
        worksheet.write_string(x, 0, color, style)

    # sešit bude uzavřen automaticky
