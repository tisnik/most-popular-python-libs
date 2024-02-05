import PySimpleGUI as sg

# ovládací prvky, které se mají zobrazit v okně
layout = [
    [sg.ProgressBar(10, orientation="h", size=(20, 20), key="progress")],
    [sg.Button("Next step")],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #45", layout)
progress_bar = window["progress"]

# obsluha smyčky událostí (event loop)
for i in range(11):
    # přečtení události
    event, values = window.read()
    print("Event: ", event, "    Values: ", values)
    progress_bar.UpdateBar(i+1)

    # reakce na událost "uzavření okna"
    if event == sg.WIN_CLOSED:
        break

# po přečtení události okno zavřeme
window.close()
