from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.button import Button


class Application(App):
    def build(self):
        layout = GridLayout(cols=1, padding=10, spacing=10)

        slider = Slider(min=0, max=100, value=25)
        layout.add_widget(slider)

        slider = Slider(min=0, max=100, value=50)
        layout.add_widget(slider)

        slider = Slider(min=0, max=100, value=75)
        layout.add_widget(slider)

        button = Button(text="Ok")
        button.on_release=self.stop
        layout.add_widget(button)

        return layout

    def on_start(self):
        Window.size = (400, 260)


if __name__ == "__main__":
    Application().run()
