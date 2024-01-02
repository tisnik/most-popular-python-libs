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
    [sg.Text("Hello, world!")],
    [sg.Submit("okay")],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #5", layout)

# čekání na uzavření okna
window.read()

# po přečtení události můžeme okno zavřít
window.close()
