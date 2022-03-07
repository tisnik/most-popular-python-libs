#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Vytvoření sešitu s několika vyplněnými buňkami."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook("example04.xlsx") as workbook:
    # vložení nového listu do sešitu
    worksheet = workbook.add_worksheet()

    # buňka s textem
    worksheet.write(0, 0, "www.root.cz")

    # buňky s numerickými hodnotami
    worksheet.write(1, 0, 6)
    worksheet.write(2, 0, 7)
    worksheet.write(2, 1, 8)

    # sešit bude uzavřen automaticky
