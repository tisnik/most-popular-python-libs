from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class Application(App):
    def build(self):
        layout = GridLayout(cols=3, padding=10, spacing=10)

        button = Button(text="1")
        layout.add_widget(button)

        button = Button(text="2")
        layout.add_widget(button)

        button = Button(text="3")
        layout.add_widget(button)

        button = Button(text="4")
        layout.add_widget(button)

        button = Button(text="5")
        layout.add_widget(button)

        button = Button(text="6")
        layout.add_widget(button)

        button = Button(text="7")
        layout.add_widget(button)

        button = Button(text="8")
        layout.add_widget(button)

        button = Button(text="9")
        layout.add_widget(button)

        return layout

    def on_start(self):
        Window.size = (200, 200)


if __name__ == "__main__":
    Application().run()
