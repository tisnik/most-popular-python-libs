import PySimpleGUI as sg

# kreslicí plátno
canvas = sg.Canvas(background_color='#ccffcc', size=(400, 400))


button_size = (10, 0)

# ovládací prvky, které se mají zobrazit v okně
left_column = [
    [sg.Button("Draw lines", size=button_size)],
    [sg.Button("Draw ellipse", size=button_size)],
    [sg.Button("Draw polyline", size=button_size)],
    [sg.Button("Draw spline", size=button_size)],
    [sg.Button("Clear canvas", size=button_size)],
    [sg.Button("Exit", size=button_size)],
]

right_column = [
    [
        canvas
    ],
]

layout = [
    [
        sg.Frame("Commands", left_column),
        sg.Frame("Canvas", right_column),
    ],
]


def draw_lines(canvas, tkcanvas):
    """Vykreslení úseček na plátno."""
    size = canvas.get_size()
    tkcanvas.create_line(0, 0, size[0]-1, size[1]-1)
    tkcanvas.create_line(0, size[1]-1, size[0]-1, 0)


def draw_ellipse(canvas, tkcanvas):
    """Vykreslení oválu na plátno."""
    border = 5
    size = canvas.get_size()
    tkcanvas.create_oval(border, border, size[0]-border, size[1]-border)


def draw_polyline(canvas, tkcanvas, smooth):
    """Vykreslení polyčáry na plátno."""
    border = 1
    size = canvas.get_size()
    tkcanvas.create_line(
            border, size[1]-border,
            size[0]/3, border,
            size[0]*2/3, size[1]-border,
            size[0]-border, border,
            smooth=smooth)


def clear_canvas(tkcanvas):
    """Vymazání všech objektů z kreslicího plátna."""
    tkcanvas.delete("all")


# vytvoření okna s ovládacími prvky
window = sg.Window("Window #32", layout, use_custom_titlebar=False, finalize=True)

# reference na plátno z knihovny Tk
tkcanvas = canvas.TKCanvas

# obsluha smyčky událostí (event loop)
while True:
    # přečtení jediné události
    event, values = window.read()
    print("Event: ", event, "    Values: ", values)

    # reakce na událost "uzavření okna"
    if event in {"Exit", sg.WIN_CLOSED}:
        break
    elif event == "Draw lines":
        draw_lines(canvas, tkcanvas)
    elif event == "Draw ellipse":
        draw_ellipse(canvas, tkcanvas)
    elif event == "Draw polyline":
        draw_polyline(canvas, tkcanvas, False)
    elif event == "Draw spline":
        draw_polyline(canvas, tkcanvas, True)
    elif event == "Clear canvas":
        clear_canvas(tkcanvas)
    window.refresh()


# po přečtení události okno zavřeme
window.close()
