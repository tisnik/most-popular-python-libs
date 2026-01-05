from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.checkbox import CheckBox
from kivy.uix.slider import Slider

for item in dir(Button):
    if "color" in item:
        print(item)
