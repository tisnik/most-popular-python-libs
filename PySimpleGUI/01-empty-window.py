import PySimpleGUI as sg

# ovládací prvky, které se mají zobrazit v okně
layout = [[]]

# vytvoření okna s ovládacími prvky
window = sg.Window("Window #1", layout, size=(320, 240))

# čekání na událost
window.read()

# po vzniku událostí aplikaci ukončíme
window.close()
