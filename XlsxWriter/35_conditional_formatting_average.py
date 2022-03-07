#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Podmíněné formátování, hodnoty pod průměrem."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook("example34.xlsx") as workbook:
    # vložení nového listu do sešitu
    worksheet = workbook.add_worksheet()

    # definice nového stylu
    bold_style = workbook.add_format()
    bold_style.set_bold()
    bold_style.set_font_color("blue")

    # definice dalšího nového stylu
    red_style = workbook.add_format()
    red_style.set_font_color("red")

    # definice dalšího nového stylu
    green_style = workbook.add_format()
    green_style.set_font_color("green")

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
    conditional_format_1 = {
        "type": "cell",
        "criteria": "between",
        "minimum": 5,
        "maximum": 15,
        "format": red_style,
    }

    # nastavení podmíněného formátu u druhého sloupce hodnot
    worksheet.conditional_format(1, 0, 20, 0, conditional_format_1)

    # formát s podmínkou
    conditional_format_2 = {
        "type": "average",
        "criteria": "above",
        "format": green_style,
    }

    # nastavení podmíněného formátu u prvního sloupce hodnot
    worksheet.conditional_format(1, 0, 20, 0, conditional_format_1)

    # nastavení podmíněného formátu u druhého sloupce hodnot
    worksheet.conditional_format(1, 1, 20, 1, conditional_format_2)

    # sešit bude uzavřen automaticky
