import PySimpleGUI as sg

# ovládací prvky, které se mají zobrazit v okně
layout = [
    [sg.Push(), sg.Image("blink.gif", key="gif"), sg.Push()],
    [sg.Push(), sg.Button("Next frame"), sg.Push()],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #50", layout)
gif = window["gif"]

# obsluha smyčky událostí (event loop)
while True:
    # přečtení události
    event, values = window.read()
    print("Event: ", event, "    Values: ", values)
    if event == "Next frame":
        gif.UpdateAnimation("blink.gif")

    # reakce na událost "uzavření okna"
    if event == sg.WIN_CLOSED:
        break


# po přečtení události okno zavřeme
window.close()
