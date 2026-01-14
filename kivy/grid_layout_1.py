# Knihovna Kivy
#
# - GUI aplikace s jediným dialogem
# - definice dialogu využívajícího GridLayout
# - použita je mřížka se třemi sloupci
# - dialog obsahuje devět tlačítek se stejnými vlastnostmi

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class Application(App):
    def build(self):
        layout = GridLayout(cols=3)

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
