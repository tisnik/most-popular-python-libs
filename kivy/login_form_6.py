from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class Application(App):
    def build(self):
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

    def on_start(self):
        Window.size = (400, 180)


if __name__ == "__main__":
    Application().run()
