# Knihovna Kivy
#
# - GUI aplikace s jediným dialogem
# - definice dialogu využívajícího BoxLayout
# - uvnitř kontejneru BoxLayout jsou umístěny další kontejnery stejného typu
# - tlačítka jsou vložena až do těchto vnitřních kontejnerů

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class Application(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        first_panel = BoxLayout(orientation="horizontal")
        button = Button(text="1")
        first_panel.add_widget(button)

        button = Button(text="2")
        first_panel.add_widget(button)

        button = Button(text="3")
        first_panel.add_widget(button)

        layout.add_widget(first_panel)

        second_panel = BoxLayout(orientation="horizontal")
        button = Button(text="4")
        second_panel.add_widget(button)

        button = Button(text="5")
        second_panel.add_widget(button)

        button = Button(text="6")
        second_panel.add_widget(button)

        button = Button(text="7")
        second_panel.add_widget(button)

        layout.add_widget(second_panel)

        third_panel = BoxLayout(orientation="horizontal")
        button = Button(text="8")
        third_panel.add_widget(button)

        button = Button(text="9")
        third_panel.add_widget(button)

        layout.add_widget(third_panel)

        return layout

    def on_start(self):
        Window.size = (400, 300)


if __name__ == "__main__":
    Application().run()
