#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Vytvoření sešitu se sloučenými buňkami."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook('example29.xlsx') as workbook:
    # vložení nového listu do sešitu
    worksheet = workbook.add_worksheet()

    # formát použitý pro zvýraznění sloučené buňky
    format1 = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#ff8080'})

    # sloučená buňka
    worksheet.merge_range('B2:D4', 'Sloučená buňka', format1)

    # sešit bude uzavřen automaticky
