import PySimpleGUI as sg

# ovládací prvky, které se mají zobrazit v okně
layout = [
    [sg.Text("Hello, world!")],
    [sg.Submit("okay")],
]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #5", layout)

# čekání na uzavření okna
window.read()

# po přečtení události můžeme okno zavřít
window.close()
