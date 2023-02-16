#!/usr/bin/env python3
# vim: set fileencoding=utf-8

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

"""Vytvoření sešitu s několika listy."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook("example25.xlsx") as workbook:
    # vytvoření několika listů
    for name in ("První", "Druhý", "Třetí", "Čtvrtý"):
        # vložení nového listu do sešitu
        worksheet = workbook.add_worksheet(name)

    # sešit bude uzavřen automaticky
