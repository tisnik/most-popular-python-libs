#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Vytvoření prázdného sešitu."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
workbook = xlsxwriter.Workbook("example01.xlsx")

# vložení nového listu do sešitu
worksheet = workbook.add_worksheet()

# explicitní uzavření sešitu
workbook.close()
