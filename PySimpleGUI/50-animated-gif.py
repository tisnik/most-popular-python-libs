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
# https://github.com/tisnik/most-popular-python-libs/blob/master/PySimpleGUI/50-animated-gif.py
#
# link to source in literate programming format:
# https://tisnik.github.io/most-popular-python-libs/PySimpleGUI/50-animated-gif.html

import PySimpleGUI as sg

# ovládací prvky, které se mají zobrazit v okně
layout = [
    [sg.Push(), sg.Image("blink.gif", key="gif"), sg.Push()],
    [sg.Push(), sg.Button("Next frame"), sg.Push()],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #50", layout)
gif = window["gif"]

# obsluha smyčky událostí (event loop)
while True:
    # přečtení události
    event, values = window.read()
    print("Event: ", event, "    Values: ", values)
    if event == "Next frame":
        gif.UpdateAnimation("blink.gif")

    # reakce na událost "uzavření okna"
    if event == sg.WIN_CLOSED:
        break


# po přečtení události okno zavřeme
window.close()
