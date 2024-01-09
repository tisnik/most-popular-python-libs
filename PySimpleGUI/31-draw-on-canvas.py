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

    # zjistit velikost plátna
    size = canvas.get_size()

    # vykreslení na plátno
    tkcanvas.create_line(0, 0, size[0] - 1, size[1] - 1)
    tkcanvas.create_line(0, size[1] - 1, size[0] - 1, 0)


# vytvoření okna s ovládacími prvky
window = sg.Window("Window #31", layout, use_custom_titlebar=False, finalize=True)

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
