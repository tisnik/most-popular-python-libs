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

"""Jednoduchý validátor."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook("example41.xlsx") as workbook:
    # vložení nového listu do sešitu
    worksheet = workbook.add_worksheet()

    # nastavení šířky sloupců a stylu
    worksheet.set_column("A:A", 50)
    worksheet.set_column("B:B", 14)

    # zápis hodnot do buněk
    worksheet.write_string("A1", "Hodnota v rozsahu 1-100:")
    worksheet.write_number("B1", 50)

    # nastavení validátoru
    worksheet.data_validation(
        "B1",
        {
            "validate": "integer",
            "criteria": "between",
            "minimum": 1,
            "maximum": 100,
            "input_title": "Celočíselná hodnota:",
            "input_message": "v rozsahu 1 až 100",
        },
    )

    # sešit bude uzavřen automaticky
