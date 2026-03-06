# Knihovna Kivy
#
# - GUI aplikace s jediným dialogem
# - definice dialogu využívajícího FloatLayout
# - dialog obsahuje devět tlačítek se stejnými vlastnostmi

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class Application(App):
    def build(self):
        layout = FloatLayout()

        button = Button(text="1", size_hint=(1/4, 1/4))
        layout.add_widget(button)

        button = Button(text="2", size_hint=(1/4, 1/4))
        layout.add_widget(button)

        button = Button(text="3", size_hint=(1/4, 1/4))
        layout.add_widget(button)

        button = Button(text="4", size_hint=(1/4, 1/4))
        layout.add_widget(button)

        button = Button(text="5", size_hint=(1/4, 1/4))
        layout.add_widget(button)

        button = Button(text="6", size_hint=(1/4, 1/4))
        layout.add_widget(button)

        button = Button(text="7", size_hint=(1/4, 1/4))
        layout.add_widget(button)

        button = Button(text="8", size_hint=(1/4, 1/4))
        layout.add_widget(button)

        button = Button(text="9", size_hint=(1/4, 1/4))
        layout.add_widget(button)

        return layout

    def on_start(self):
        Window.size = (200, 200)


if __name__ == "__main__":
    Application().run()
