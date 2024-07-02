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
    [sg.Push(), sg.Image("progress.gif", key="gif"), sg.Push()],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #51", layout)
gif = window["gif"]

# obsluha smyčky událostí (event loop)
while True:
    # přečtení události
    event, values = window.read(timeout=50)
    print("Event: ", event, "    Values: ", values)
    gif.UpdateAnimation("progress.gif")

    # reakce na událost "uzavření okna"
    if event == sg.WIN_CLOSED:
        break


# po přečtení události okno zavřeme
window.close()
