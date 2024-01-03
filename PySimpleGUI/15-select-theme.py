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

themes = sorted(sg.list_of_look_and_feel_values())


# vytvoření okna s ovládacími prvky
def main_window(theme=None):
    selected_theme = theme or themes[0]

    # ovládací prvky, které se mají zobrazit v okně
    layout = [
        [
            sg.Text("Theme"),
            sg.Combo(themes, default_value=selected_theme, readonly=True, key="theme"),
        ],
        [
            sg.Button("Change"),
            sg.Cancel("Exit")
        ],
    ]

    sg.theme(selected_theme)
    return sg.Window("Window #4", layout)


window = main_window()

# obsluha smyčky událostí (event loop)
while True:
    # přečtení události
    event, values = window.read()

    # reakce na událost "uzavření okna"
    if event in {sg.WIN_CLOSED, "Exit"}:
        break

    # reakce na výběr tématu
    if event == "Change":
        selected_theme = values["theme"]
        window.close()
        window = main_window(selected_theme)

# po výskoku ze smyčky událostí aplikaci ukončíme
window.close()
