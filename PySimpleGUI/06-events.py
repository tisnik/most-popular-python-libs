import PySimpleGUI as sg

# ovládací prvky, které se mají zobrazit v okně
layout = [
    [sg.Text("Hello, world!"), sg.Button("Button1")],
    [sg.InputText()],
    [sg.Submit(), sg.Cancel()],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #6", layout)

# obsluha smyčky událostí (event loop)
while True:
    # přečtení události
    event, values = window.read()
    print("Event: ", event, "    Values: ", values)

    # reakce na událost "uzavření okna"
    if event == sg.WIN_CLOSED:
        break

# po výskoku ze smyčky událostí aplikaci ukončíme
window.close()
