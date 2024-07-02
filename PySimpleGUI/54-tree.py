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

data = sg.TreeData()

data.Insert("", "A", "A", [])
data.Insert("", "B", "B", [])
data.Insert("", "C", "D", [])
data.Insert("A", "A1", "A1", [])
data.Insert("A", "A2", "A2", [])
data.Insert("A", "A3", "A3", [])
data.Insert("B", "B1", "B1", [])
data.Insert("B", "B2", "B2", [])
data.Insert("B", "B3", "B3", [])
data.Insert("C", "C1", "C1", [])
data.Insert("C", "C2", "C2", [])
data.Insert("C", "C3", "C3", [])


# ovládací prvky, které se mají zobrazit v okně
layout = [
    [sg.Tree(data=data, headings=[""])],
    [sg.Push(), sg.Submit(), sg.Push()],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #54", layout)

# přečtení jediné události
event, values = window.read()
print("Event: ", event, "    Values: ", values)

# po přečtení události okno zavřeme
window.close()
