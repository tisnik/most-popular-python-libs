#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Vytvoření sešitu s delší tabulkou, nastavení šířky sloupců."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook('example06.xlsx') as workbook:
    # vložení nového listu do sešitu
    worksheet = workbook.add_worksheet()

    # nastavení šířky sloupců
    worksheet.set_column('A:A', 8)
    worksheet.set_column('B:B', 14)
    worksheet.set_column('C:Z', 2)

    # buňky s textem
    worksheet.write('A1', 'x')
    worksheet.write('B1', '1/x')

    # buňky s numerickými hodnotami
    for x in range(1, 21):
        worksheet.write(x, 0, x)
        worksheet.write(x, 1, 1.0/x)

    # sešit bude uzavřen automaticky
