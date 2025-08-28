# Knihovna PySimpleGUI
#
# - otevření jednoduchého okna
# - přidání většího množství ovládacích prvků do okna
# - automatická změna velikosti okna
# - realizace smyčky pro obsluhu událostí (event loop)

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
# https://github.com/tisnik/most-popular-python-libs/blob/master/PySimpleGUI/05-more-controls.py
#
# link to source in literate programming format:
# https://tisnik.github.io/most-popular-python-libs/PySimpleGUI/05-more-controls.html

import PySimpleGUI as sg

# ovládací prvky, které se mají zobrazit v okně
layout = [
    [sg.Text("Hello, world!"), sg.Button("Button1")],
    [sg.InputText()],
    [sg.Submit(), sg.Cancel()],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #4", layout)

# obsluha smyčky událostí (event loop)
while True:
    # přečtení události
    event, values = window.read()

    # reakce na událost "uzavření okna"
    if event == sg.WIN_CLOSED:
        break

# po výskoku ze smyčky událostí aplikaci ukončíme
window.close()
