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
layout = [
    [
        sg.Button("Button1", key=1),
        sg.Button("Button2", key=2),
    ],
    [
        sg.Push(),
        sg.Button("Button1", key=3),
        sg.Button("Button2", key=4),
    ],
    [
        sg.Button("Button1", key=5),
        sg.Push(),
        sg.Button("Button2", key=6),
    ],
    [
        sg.Button("Button1", key=7),
        sg.Button("Button2", key=8),
        sg.Push(),
    ],
    [
        sg.Push(),
        sg.Button("Button1", key=9),
        sg.Button("Button2", key=10),
        sg.Push(),
    ],
    [
        sg.Push(),
        sg.Button("Button1", key=11),
        sg.Push(),
        sg.Button("Button2", key=12),
        sg.Push(),
    ],
    [sg.Submit(key=13)],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #38", layout, size=(320, 260), resizable=True, finalize=True)

for i in range(1, 14):
    window[i].expand(expand_x=True, expand_y=True)

# přečtení jediné události
event, values = window.read()
print("Event: ", event, "    Values: ", values)

# po přečtení události okno zavřeme
window.close()
