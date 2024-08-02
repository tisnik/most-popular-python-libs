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
# https://github.com/tisnik/most-popular-python-libs/blob/master/PySimpleGUI/36-line-dashes.py
#
# link to source in literate programming format:
# https://tisnik.github.io/most-popular-python-libs/PySimpleGUI/36-line-dashes.html


import PySimpleGUI as sg

# kreslicí plátno
canvas = sg.Canvas(background_color="#ccffcc", size=(400, 400))


# ovládací prvky, které se mají zobrazit v okně
left_column = [
    [sg.Button("Draw lines", size=(8, 0))],
    [sg.Button("Exit", size=(8, 0))],
]

right_column = [
    [canvas],
]

layout = [
    [
        sg.Frame("Commands", left_column),
        sg.Frame("Canvas", right_column),
    ],
]


def draw_lines(canvas):
    """Vykreslení úseček na plátno."""
    # reference na plátno z knihovny Tk
    tkcanvas = canvas.TKCanvas

    # úsečky s nastavenými grafickými vlastnostmi
    tkcanvas.create_line(10, 10, 90, 90)
    tkcanvas.create_line(110, 10, 190, 90, fill="#8080ff")
    tkcanvas.create_line(210, 10, 290, 90, fill="#ffff80", width=8)
    tkcanvas.create_line(310, 10, 390, 90, fill="#80aa80", width=8, dash=15)

    tkcanvas.create_line(10, 110, 90, 190, width=2, dash=(12, 3))
    tkcanvas.create_line(110, 110, 190, 190, width=2, dash=(9, 6))
    tkcanvas.create_line(210, 110, 290, 190, width=2, dash=(6, 9))
    tkcanvas.create_line(310, 110, 390, 190, width=2, dash=(3, 12))

    tkcanvas.create_line(10, 210, 90, 290, width=2, dash=(12, 2, 2, 2))
    tkcanvas.create_line(110, 210, 190, 290, width=2, dash=(12, 2, 4, 2))
    tkcanvas.create_line(210, 210, 290, 290, width=2, dash=(12, 4, 2, 4))
    tkcanvas.create_line(310, 210, 390, 290, width=2, dash=(12, 2, 2, 2, 2, 2))

    tkcanvas.create_line(10, 310, 90, 390, width=2, dash=(12, 2, 2, 2), dashoff=0)
    tkcanvas.create_line(110, 310, 190, 390, width=2, dash=(12, 2, 4, 2), dashoff=5)
    tkcanvas.create_line(210, 310, 290, 390, width=2, dash=(12, 4, 2, 4), dashoff=10)
    tkcanvas.create_line(
        310, 310, 390, 390, width=2, dash=(12, 2, 2, 2, 2, 2), dashoff=-5
    )


# vytvoření okna s ovládacími prvky
window = sg.Window("Window #36", layout, use_custom_titlebar=False, finalize=True)

# obsluha smyčky událostí (event loop)
while True:
    # přečtení jediné události
    event, values = window.read()
    print("Event: ", event, "    Values: ", values)

    # reakce na událost "uzavření okna"
    if event in {"Exit", sg.WIN_CLOSED}:
        break
    elif event == "Draw lines":
        draw_lines(canvas)
        window.refresh()

# po přečtení události okno zavřeme
window.close()
