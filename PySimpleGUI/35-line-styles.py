import PySimpleGUI as sg
import tkinter

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

    tkcanvas.create_line(10, 110, 90, 190, fill="red", width=12)
    tkcanvas.create_line(110, 110, 190, 190, fill="red", width=12, cap=tkinter.BUTT)
    tkcanvas.create_line(
        210, 110, 290, 190, fill="red", width=12, cap=tkinter.PROJECTING
    )
    tkcanvas.create_line(310, 110, 390, 190, fill="red", width=12, cap=tkinter.ROUND)

    tkcanvas.create_line(10, 110, 90, 190, fill="white")
    tkcanvas.create_line(110, 110, 190, 190, fill="white")
    tkcanvas.create_line(210, 110, 290, 190, fill="white")
    tkcanvas.create_line(310, 110, 390, 190, fill="white")

    tkcanvas.create_line(10, 210, 50, 290, 90, 210, fill="red", width=12)
    tkcanvas.create_line(
        110, 210, 150, 290, 190, 210, fill="red", width=12, cap=tkinter.BUTT
    )
    tkcanvas.create_line(
        210, 210, 250, 290, 290, 210, fill="red", width=12, cap=tkinter.PROJECTING
    )
    tkcanvas.create_line(
        310, 210, 350, 290, 390, 210, fill="red", width=12, cap=tkinter.ROUND
    )

    # pomocné úsečky
    tkcanvas.create_line(10, 210, 50, 290, 90, 210, fill="white")
    tkcanvas.create_line(110, 210, 150, 290, 190, 210, fill="white")
    tkcanvas.create_line(210, 210, 250, 290, 290, 210, fill="white")
    tkcanvas.create_line(310, 210, 350, 290, 390, 210, fill="white")

    tkcanvas.create_line(10, 310, 50, 390, 90, 310, fill="red", width=12)
    tkcanvas.create_line(
        110, 310, 150, 390, 190, 310, fill="red", width=12, join=tkinter.ROUND
    )
    tkcanvas.create_line(
        210, 310, 250, 390, 290, 310, fill="red", width=12, join=tkinter.BEVEL
    )
    tkcanvas.create_line(
        310, 310, 350, 390, 390, 310, fill="red", width=12, join=tkinter.MITER
    )

    # pomocné úsečky
    tkcanvas.create_line(10, 310, 50, 390, 90, 310, fill="white")
    tkcanvas.create_line(110, 310, 150, 390, 190, 310, fill="white")
    tkcanvas.create_line(210, 310, 250, 390, 290, 310, fill="white")
    tkcanvas.create_line(310, 310, 350, 390, 390, 310, fill="white")


# vytvoření okna s ovládacími prvky
window = sg.Window("Window #35", layout, use_custom_titlebar=False, finalize=True)

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
