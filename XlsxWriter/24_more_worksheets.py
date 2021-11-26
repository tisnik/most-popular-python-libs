#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Vytvoření sešitu s několika listy."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook('example24.xlsx') as workbook:
    # vytvoření několika listů
    for name in range(4):
        # vložení nového listu do sešitu
        worksheet = workbook.add_worksheet()

    # sešit bude uzavřen automaticky
