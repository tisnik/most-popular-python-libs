import PySimpleGUI as sg

# ovládací prvky, které se mají zobrazit v okně
layout = [
    [sg.Text("Option menu"), sg.OptionMenu(["Alpher", "Bethe", "Gamow",], s=(15, 2))],
    [sg.Submit()],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #47", layout)

# přečtení jediné události
event, values = window.read()
print("Event: ", event, "    Values: ", values)

# po přečtení události okno zavřeme
window.close()
