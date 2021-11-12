#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Vytvoření prázdného sešitu, zajištění uzavření objektu worksheet."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook('example02.xlsx') as workbook:
    # vložení nového listu do sešitu
    worksheet = workbook.add_worksheet()
    # sešit bude uzavřen automaticky
