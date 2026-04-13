# Knihovna Kivy
#
# - GUI aplikace s jediným dialogem
# - definice dialogu využívajícího PageLayout
# - PageLayout využívá výchozí (horizontální) orientaci
# - dialog obsahuje trojici stránek s tlačítky

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.pagelayout import PageLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button


class Application(App):
    def build(self):
        layout = PageLayout()

        layout1 = AnchorLayout()
        button = Button(text="1", size_hint=(0.5, 0.5))
        layout1.add_widget(button)
        layout.add_widget(layout1)

        layout2 = AnchorLayout()
        button = Button(text="2", size_hint=(0.5, 0.5))
        layout2.add_widget(button)
        layout.add_widget(layout2)

        layout3 = AnchorLayout()
        button = Button(text="3", size_hint=(0.5, 0.5))
        layout3.add_widget(button)
        layout.add_widget(layout3)

        return layout

    def on_start(self):
        Window.size = (400, 300)


if __name__ == "__main__":
    Application().run()
