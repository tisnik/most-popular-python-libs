#
#  (C) Copyright 2024  Pavel Tisnovsky
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
# https://github.com/tisnik/most-popular-python-libs/blob/master/PySimpleGUI/53-table.py
#
# link to source in literate programming format:
# https://tisnik.github.io/most-popular-python-libs/PySimpleGUI/53-table.html

import PySimpleGUI as sg

data = [
        ["Jan 2024", "Jan 2023", "Language", "Ratings", "Change"],
        [1, 1, "Python", "13.97%", "-2.39%"],
        [2, 2, "C", "11.44%", "-4.81%"],
        [3, 3, "C++", "9.96%", "-2.95%"],
        [4, 4, "Java", "7.87%", "-4.34%"],
        [5, 5, "C#", "7.16%", "+1.43%"],
        [6, 7, "JavaScript", "2.77%", "-0.11%"],
        ]

# ovládací prvky, které se mají zobrazit v okně
layout = [
    [sg.Table(data)],
    [sg.Push(), sg.Submit(), sg.Push()],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #53", layout)

# přečtení jediné události
event, values = window.read()
print("Event: ", event, "    Values: ", values)

# po přečtení události okno zavřeme
window.close()
