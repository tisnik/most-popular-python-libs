# Knihovna Kivy
#
# - GUI aplikace s jediným dialogem
# - definice dialogu využívajícího PageLayout
# - PageLayout využívá výchozí (horizontální) orientaci
# - dialog obsahuje trojici stránek s tlačítky

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.pagelayout import PageLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.slider import Slider


def login_page():
    layout = GridLayout(cols=2, padding=10, spacing=10)

    # prvni radek mrizky
    label1 = Label(text="Name")
    layout.add_widget(label1)
    username = TextInput(multiline=False)
    layout.add_widget(username)

    # druhy radek mrizky
    label2 = Label(text="Password")
    layout.add_widget(label2)
    password1 = TextInput(password=True, multiline=False)
    layout.add_widget(password1)

    # treti radek mrizky
    label3 = Label(text="Confirm password")
    layout.add_widget(label3)
    password2 = TextInput(password=True, multiline=False)
    layout.add_widget(password2)

    # ctvrty radek mrizky
    button = Button(text="Login")
    layout.add_widget(button)

    return layout


def color_page():
    layout = GridLayout(cols=5, padding=10, spacing=10)

    slider_red = Slider(min=0, max=100, value=25, orientation="vertical")
    layout.add_widget(slider_red)

    slider_green = Slider(min=0, max=100, value=50, orientation="vertical")
    layout.add_widget(slider_green)

    slider_blue = Slider(min=0, max=100, value=75, orientation="vertical")
    layout.add_widget(slider_blue)

    label_rgb = Label(text="[size=40pt][b]T\ne\ns\nt[/b][/size]", markup=True)
    layout.add_widget(label_rgb)

    button = Button(text="Ok")
    layout.add_widget(button)

    return layout


class Application(App):
    def build(self):
        layout = PageLayout()
        layout.add_widget(login_page())
        layout.add_widget(color_page())

        return layout

    def on_start(self):
        Window.size = (400, 300)


if __name__ == "__main__":
    Application().run()
