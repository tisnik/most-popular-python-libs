import PySimpleGUI as sg

# ovládací prvky, které se mají zobrazit v okně
layout = [
    [sg.Image("globe.png")],
    [sg.Push(), sg.Submit(), sg.Push()],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #49", layout)

# přečtení jediné události
event, values = window.read()
print("Event: ", event, "    Values: ", values)

# po přečtení události okno zavřeme
window.close()
