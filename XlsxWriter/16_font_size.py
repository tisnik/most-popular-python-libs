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

"""Vytvoření sešitu s delší tabulkou, změna velikosti fontu."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook("example16.xlsx") as workbook:
    # vložení nového listu do sešitu
    worksheet = workbook.add_worksheet()

    # nastavení šířky sloupců
    worksheet.set_column("A:A", 20)

    # buňky s numerickými hodnotami a různou velikostí textu
    for x in range(1, 21):
        style = workbook.add_format()
        style.set_font_size(x)
        worksheet.write_number(x, 0, x, style)

    # sešit bude uzavřen automaticky
