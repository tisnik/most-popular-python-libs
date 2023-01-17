#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2023  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import polars

# přečtení zdrojových dat
df = polars.read_csv("hall_of_fame.csv")

# maximální počet zobrazených řádků
polars.Config.set_tbl_rows(100)

formattings = (
        "ASCII_FULL",
        "ASCII_FULL_CONDENSED",
        "ASCII_NO_BORDERS",
        "ASCII_BORDERS_ONLY",
        "ASCII_BORDERS_ONLY_CONDENSED",
        "ASCII_HORIZONTAL_ONLY",
        "ASCII_MARKDOWN",
        "UTF8_FULL",
        "UTF8_FULL_CONDENSED",
        "UTF8_NO_BORDERS",
        "UTF8_BORDERS_ONLY",
        "UTF8_HORIZONTAL_ONLY",
        "NOTHING",
        )

for formatting in formattings:
    print()
    print(formatting)
    print()

    polars.Config.set_tbl_formatting(formatting)

    # zobrazíme datový rámec
    print(df)
