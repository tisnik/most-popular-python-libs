import PySimpleGUI as sg

# ovládací prvky, které se mají zobrazit v okně
layout = [
    [
        sg.Button("S"),
    ],
    [
        sg.Button("Button"),
    ],
    [
        sg.Button("Long button"),
    ],
    [sg.Submit()],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #17", layout)

# přečtení jediné události
event, values = window.read()
print("Event: ", event, "    Values: ", values)

# po přečtení události okno zavřeme
window.close()
