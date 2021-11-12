#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Vytvoření sešitu s delší tabulkou, nastavení barvy textu."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook('example18.xlsx') as workbook:
    # vložení nového listu do sešitu
    worksheet = workbook.add_worksheet()

    # nastavení šířky sloupců
    worksheet.set_column('A:A', 20)

    # barvy buněk
    colors = (
            '#000000',
            '#0000ff',
            '#800000',
            '#00ffff',
            '#808080',
            '#008000',
            '#00ff00',
            '#ff00ff',
            '#000080',
            '#ff6600',
            '#ff00ff',
            '#800080',
            '#ff0000',
            '#c0c0c0',
            '#ffffff',
            '#ffff00',
            )

    # buňky s řetězci a různou barvou textu
    for x, color in enumerate(colors):
        style = workbook.add_format()
        style.set_font_color(color)
        worksheet.write_string(x, 0, color, style)

    # sešit bude uzavřen automaticky
