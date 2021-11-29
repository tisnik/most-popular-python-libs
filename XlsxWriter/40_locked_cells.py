#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Uzamčení buněk."""

import xlsxwriter

# vytvoření objektu reprezentujícího celý sešit
with xlsxwriter.Workbook('example40.xlsx') as workbook:
    # vložení nového listu do sešitu
    worksheet = workbook.add_worksheet()

    # uzamčení sešitu
    worksheet.protect()

    # definice nového stylu
    bold_style = workbook.add_format()
    bold_style.set_bold()
    bold_style.set_font_color('blue')

    # definice dalšího nového stylu
    locked_style = workbook.add_format()
    locked_style.set_font_color('red')

    # buňky budou uzamčeny
    locked_style.set_locked('True')

    # definice dalšího nového stylu
    unlocked_style = workbook.add_format()

    # buňky budou uzamčeny
    unlocked_style.set_locked('False')

    # definice formátu čísel
    numeric_format = workbook.add_format({'num_format': '0.0000'})

    # nastavení šířky sloupců a stylu
    worksheet.set_column('A:A', 8)
    worksheet.set_column('B:B', 14, numeric_format)
    worksheet.set_column('C:Z', 20)

    # styl pro první řádek
    worksheet.set_row(0, 20, bold_style)

    # buňky s textem
    worksheet.write_string('A1', 'x')
    worksheet.write_string('B1', '1/x')
    worksheet.write_string('C1', 'valid?')

    # buňky s numerickými hodnotami
    for x in range(1, 21):
        worksheet.write_number(x, 0, x, locked_style)
        worksheet.write_number(x, 1, 1.0/x)
        msg = "yes" if x % 2 == 0 else "no"
        worksheet.write_string(x, 2, msg, unlocked_style)

    # nastavení automatického filtru
    worksheet.autofilter('A1:C21')

    # sešit bude uzavřen automaticky
