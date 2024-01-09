import PySimpleGUI as sg

# ovládací prvky, které se mají zobrazit v okně
left_column = [
    [sg.Button("Exit", size=(8, 0))],
]

right_column = [
    [
        sg.Canvas(background_color="white", size=(320, 240)),
    ],
]

layout = [
    [
        sg.Frame("Commands", left_column),
        sg.Frame("Canvas", right_column),
    ],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #29", layout, use_custom_titlebar=False)

# přečtení jediné události
event, values = window.read()
print("Event: ", event, "    Values: ", values)

# po přečtení události okno zavřeme
window.close()
