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
# https://github.com/tisnik/most-popular-python-libs/blob/master/PySimpleGUI/20-push.py
#
# link to source in literate programming format:
# https://tisnik.github.io/most-popular-python-libs/PySimpleGUI/20-push.html

import PySimpleGUI as sg

# ovládací prvky, které se mají zobrazit v okně
layout = [
    [
        sg.Button("Button1"),
        sg.Button("Button2"),
    ],
    [
        sg.Push(),
        sg.Button("Button1"),
        sg.Button("Button2"),
    ],
    [
        sg.Button("Button1"),
        sg.Push(),
        sg.Button("Button2"),
    ],
    [
        sg.Button("Button1"),
        sg.Button("Button2"),
        sg.Push(),
    ],
    [
        sg.Push(),
        sg.Button("Button1"),
        sg.Button("Button2"),
        sg.Push(),
    ],
    [
        sg.Push(),
        sg.Button("Button1"),
        sg.Push(),
        sg.Button("Button2"),
        sg.Push(),
    ],
    [sg.Submit()],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #20", layout, size=(320, 260))

# přečtení jediné události
event, values = window.read()
print("Event: ", event, "    Values: ", values)

# po přečtení události okno zavřeme
window.close()
