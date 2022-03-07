#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Vytvoření sešitu s delší tabulkou, nastavení barvy pozadí."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook("example19.xlsx") as workbook:
    # vložení nového listu do sešitu
    worksheet = workbook.add_worksheet()

    # nastavení šířky sloupců
    worksheet.set_column("A:A", 20)

    # barvy buněk
    colors = (
        "black",
        "blue",
        "brown",
        "cyan",
        "gray",
        "green",
        "lime",
        "magenta",
        "navy",
        "orange",
        "pink",
        "purple",
        "red",
        "silver",
        "white",
        "yellow",
    )

    # buňky s řetězci a různou barvou pozadí buněk
    for x, color in enumerate(colors):
        style = workbook.add_format()
        style.set_bg_color(color)
        worksheet.write_string(x, 0, color, style)

    # sešit bude uzavřen automaticky
