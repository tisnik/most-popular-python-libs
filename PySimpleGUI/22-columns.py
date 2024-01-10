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
    [sg.Text("Name", size=(8, 0)), sg.InputText(key="name", size=(20, 0))],
    [sg.Text("Surname", size=(8, 0)), sg.InputText(key="surname", size=(20, 0))],
]

right_column = [
    [
        sg.Text("Role", size=(8, 0)),
        sg.Combo(
            ["Administrator", "Maintainer", "Guest"],
            default_value="Guest",
            readonly=True,
            key="role",
        ),
    ],
    [
        sg.Text("Register e-mail", size=(8, 0)),
        sg.Checkbox("", default=True, key="register e-mail"),
    ],
    [
        sg.Text("Color theme", size=(8, 0)),
        sg.Column(
            [
                [sg.Radio("Light", "THEME", default=False, key="light_theme")],
                [sg.Radio("Dark", "THEME", default=True, key="dark_theme")],
            ]
        ),
    ],
]

layout = [
    [
        sg.Column(left_column),
        sg.Column(right_column),
    ],
    [
        sg.Push(),
        sg.Submit(),
        sg.Push(),
    ],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #22", layout)

# přečtení jediné události
event, values = window.read()
print("Event: ", event, "    Values: ", values)

# po přečtení události okno zavřeme
window.close()
