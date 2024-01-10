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

import PySimpleGUI as sg

# ovládací prvky, které se mají zobrazit v okně
left_column = [
    [sg.Button("Exit", size=(8, 0))],
]

right_column = [
    [
        sg.Canvas(),
    ],
]

layout = [
    [
        sg.Frame("Commands", left_column),
        sg.Frame("Canvas", right_column),
    ],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #29", layout, use_custom_titlebar=False)

# přečtení jediné události
event, values = window.read()
print("Event: ", event, "    Values: ", values)

# po přečtení události okno zavřeme
window.close()
