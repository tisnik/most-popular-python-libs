#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Vytvoření sešitu s několika vyplněnými buňkami."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook('example03.xlsx') as workbook:
    # vložení nového listu do sešitu
    worksheet = workbook.add_worksheet()

    # buňka s textem
    worksheet.write('A1', 'www.root.cz')

    # buňky s numerickými hodnotami
    worksheet.write('A2', 6)
    worksheet.write('A3', 7)
    worksheet.write('B3', 8)

    # sešit bude uzavřen automaticky
