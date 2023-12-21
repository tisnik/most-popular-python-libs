import PySimpleGUI as sg

# ovládací prvky, které se mají zobrazit v okně
layout = [[sg.Text("Hello, world!")]]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #3", layout)

# obsluha smyčky událostí (event loop)
while True:
    # přečtení události
    event, values = window.read()

    # reakce na událost "uzavření okna"
    if event == sg.WIN_CLOSED:
        break

# po výskoku ze smyčky událostí aplikaci ukončíme
window.close()
