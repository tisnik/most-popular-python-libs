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
        DISTANCE=65

        layout = FloatLayout()

        button = Button(text="1", size_hint=(1/4, 1/4), pos=(BORDER, BORDER))
        layout.add_widget(button)

        button = Button(text="2", size_hint=(1/4, 1/4), pos=(BORDER+DISTANCE, BORDER))
        layout.add_widget(button)

        button = Button(text="3", size_hint=(1/4, 1/4), pos=(BORDER+DISTANCE*2, BORDER))
        layout.add_widget(button)

        button = Button(text="4", size_hint=(1/4, 1/4), pos=(BORDER, BORDER+DISTANCE))
        layout.add_widget(button)

        button = Button(text="5", size_hint=(1/4, 1/4), pos=(BORDER+DISTANCE, BORDER+DISTANCE))
        layout.add_widget(button)

        button = Button(text="6", size_hint=(1/4, 1/4), pos=(BORDER+DISTANCE*2, BORDER+DISTANCE))
        layout.add_widget(button)

        button = Button(text="7", size_hint=(1/4, 1/4), pos=(BORDER, BORDER+DISTANCE*2))
        layout.add_widget(button)

        button = Button(text="8", size_hint=(1/4, 1/4), pos=(BORDER+DISTANCE, BORDER+DISTANCE*2))
        layout.add_widget(button)

        button = Button(text="9", size_hint=(1/4, 1/4), pos=(BORDER+DISTANCE*2, BORDER+DISTANCE*2))
        layout.add_widget(button)

        return layout

    def on_start(self):
        Window.size = (200, 200)


if __name__ == "__main__":
    Application().run()
