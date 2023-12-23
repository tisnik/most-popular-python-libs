import PySimpleGUI as sg

themes = sorted(sg.list_of_look_and_feel_values())

print("\n".join(themes))
