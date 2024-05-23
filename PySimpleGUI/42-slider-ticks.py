import PySimpleGUI as sg

# ovládací prvky, které se mají zobrazit v okně
layout = [
    [sg.Text("Slider"),
     sg.Slider((0, 10), orientation="h", tick_interval=1, s=(20, 15), key="slider")],
    [sg.Submit()],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #42", layout)

# přečtení jediné události
event, values = window.read()
print("Event: ", event, "    Values: ", values)

# po přečtení události okno zavřeme
window.close()
