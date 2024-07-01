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
    [sg.ProgressBar(10, orientation="h", size=(20, 20), key="progress")],
    [sg.Button("Next step")],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #45", layout)
progress_bar = window["progress"]

# obsluha smyčky událostí (event loop)
for i in range(11):
    # přečtení události
    event, values = window.read()
    print("Event: ", event, "    Values: ", values)
    progress_bar.UpdateBar(i+1)

    # reakce na událost "uzavření okna"
    if event == sg.WIN_CLOSED:
        break

# po přečtení události okno zavřeme
window.close()
