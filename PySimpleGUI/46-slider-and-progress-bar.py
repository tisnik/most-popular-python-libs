import PySimpleGUI as sg

# ovládací prvky, které se mají zobrazit v okně
layout = [
    [sg.Slider((0, 10), orientation='h', tick_interval=1, s=(25, 15), default_value=0, key="slider")],
    [sg.ProgressBar(10, orientation="h", size=(20, 20), key="progress")],
    [sg.Button("Update")],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #46", layout)
progress_bar = window["progress"]
slider = window["slider"]

# obsluha smyčky událostí (event loop)
while True:
    # přečtení události
    event, values = window.read()
    print("Event: ", event, "    Values: ", values)

    # reakce na událost "uzavření okna"
    if event == sg.WIN_CLOSED:
        break

    # změna hodnoty na progress baru
    value = values["slider"]
    progress_bar.UpdateBar(value)

# po přečtení události okno zavřeme
window.close()
