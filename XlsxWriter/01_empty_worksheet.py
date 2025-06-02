#!/usr/bin/env python3
# vim: set fileencoding=utf-8
#
# Knihovna XLSXWriter
#
# - vytvoření prázdného sešitu

#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#
#
# link to source:
# https://github.com/tisnik/most-popular-python-libs/blob/master/PySimpleGUI/01_empty_worksheet.py
#
# link to source in literate programming format:
# https://tisnik.github.io/most-popular-python-libs/PySimpleGUI/01_empty_worksheet.html

"""Vytvoření prázdného sešitu."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
workbook = xlsxwriter.Workbook("example01.xlsx")

# vložení nového listu do sešitu
worksheet = workbook.add_worksheet()

# explicitní uzavření sešitu
workbook.close()
