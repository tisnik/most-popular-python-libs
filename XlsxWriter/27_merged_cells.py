#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Vytvoření sešitu se sloučenými buňkami."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook('example27.xlsx') as workbook:
    # vložení nového listu do sešitu
    worksheet = workbook.add_worksheet()

    # první formát použitý pro zvýraznění sloučené buňky
    format1 = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#ff8080'})

    # druhý formát použitý pro zvýraznění sloučené buňky
    format2 = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#80ff80'})

    # sloučená buňka
    worksheet.merge_range('B2:D2', 'Sloučená buňka', format1)

    # sloučená buňka
    worksheet.merge_range('F2:F4', 'Sloučená\nbuňka', format2)

    # sešit bude uzavřen automaticky
