from kivy.uix.button import Button

for item in dir(Button):
    if "color" in item:
        print(item)
