# Knihovna Kivy
#
# - GUI aplikace s jediným dialogem
# - definice dialogu využívajícího FloatLayout
# - dialog obsahuje devět tlačítek se stejnými vlastnostmi
# - explicitní rozmístění tlačítek

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class Application(App):
    def build(self):
        BORDER=10
        DISTANCE=30

        layout = FloatLayout()

        for i in range(0, 9):
            button = Button(text=str(i+1), size_hint=(1/6, 1/6), pos=(BORDER+DISTANCE*i, BORDER+DISTANCE*i))
            layout.add_widget(button)

        return layout

    def on_start(self):
        Window.size = (300, 300)


if __name__ == "__main__":
    Application().run()
