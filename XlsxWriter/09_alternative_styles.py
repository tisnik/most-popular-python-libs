#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Vytvoření sešitu s delší tabulkou, nastavení stylů vybraných buněk."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook('example09.xlsx') as workbook:
    # vložení nového listu do sešitu
    worksheet = workbook.add_worksheet()

    # nastavení šířky sloupců
    worksheet.set_column('A:A', 8)
    worksheet.set_column('B:B', 14)
    worksheet.set_column('C:Z', 2)

    # definice nového stylu
    bold_style = workbook.add_format()
    bold_style.set_bold()
    bold_style.set_font_color('blue')

    # buňky s textem
    worksheet.write('A1', 'x', bold_style)
    worksheet.write('B1', '1/x', bold_style)

    # buňky s numerickými hodnotami
    for x in range(1, 21):
        worksheet.write(x, 0, x)
        worksheet.write(x, 1, 1.0/x)

    # sešit bude uzavřen automaticky
