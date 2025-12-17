from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LoginScreen(GridLayout):
    def __init__(self, **var_args):

        super(LoginScreen, self).__init__(**var_args)
        self.cols = 2
        self.padding = 10
        self.spacing = 10

        # prvni radek mrizky
        self.add_widget(Label(text="Name"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        # druhy radek mrizky
        self.add_widget(Label(text="Password"))
        self.password1 = TextInput(password=True, multiline=False)
        self.add_widget(self.password1)

        # treti radek mrizky
        self.add_widget(Label(text="Confirm password"))
        self.password2 = TextInput(password=True, multiline=False)
        self.add_widget(self.password2)

        # ctvrty radek mrizky
        self.button = Button(text="Login")
        self.add_widget(self.button)


class Application(App):
    def build(self):
        return LoginScreen()

    def on_start(self):
        Window.size = (400, 180)


if __name__ == "__main__":
    Application().run()
