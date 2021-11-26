#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Vytvoření sešitu s několika listy."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook('example25.xlsx') as workbook:
    # vytvoření několika listů
    for name in ("První", "Druhý", "Třetí", "Čtvrtý"):
        # vložení nového listu do sešitu
        worksheet = workbook.add_worksheet(name)

    # sešit bude uzavřen automaticky
