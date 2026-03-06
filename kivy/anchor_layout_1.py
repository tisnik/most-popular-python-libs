# Knihovna Kivy
#
# - GUI aplikace s jediným dialogem
# - definice dialogu využívajícího AnchorLayout
# - dialog obsahuje jediné tlačítko, které je vycentrované

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button


class Application(App):
    def build(self):
        layout = AnchorLayout()

        button = Button(text="Click!", size_hint=(0.5, 0.5))
        layout.add_widget(button)

        return layout

    def on_start(self):
        Window.size = (400, 300)


if __name__ == "__main__":
    Application().run()
