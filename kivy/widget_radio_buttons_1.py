from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.button import Button


class Application(App):
    def build(self):
        layout = GridLayout(cols=2, padding=10, spacing=10)

        colors = ("Black", "Red", "Green", "Blue", "Cyan", "Magenta", "Yellow", "White")

        for color in colors:
            label = Label(text=color)
            layout.add_widget(label)
            color = CheckBox()
            layout.add_widget(color)

        button = Button(text="Ok")
        button.on_release=self.stop
        layout.add_widget(button)

        return layout

    def on_start(self):
        Window.size = (300, 360)


if __name__ == "__main__":
    Application().run()
