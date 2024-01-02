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
    [sg.Text("Name", size=(8, 0)), sg.InputText(key="name")],
    [sg.Text("Surname", size=(8, 0)), sg.InputText(key="surname")],
    [sg.Submit()],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #9", layout)

# přečtení jediné události
event, values = window.read()
print("Event: ", event, "    Values: ", values)

# po přečtení události okno zavřeme
window.close()
