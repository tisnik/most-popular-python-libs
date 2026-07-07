# Knihovna Kivy
#
# - GUI aplikace s jediným oknem
# - v okně je umístěna kreslicí plocha
# - vykreslení barevného obdélníka
# - kreslení do canvasu s využitím metody add

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color


class BasicCanvas(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.canvas.add(Color(0.9, 0.3, 0.3, 1))
        self.canvas.add(Rectangle(pos=(100, 100), size=(100, 100)))


class Application(App):
    def build(self):
        return BasicCanvas()

    def on_start(self):
        Window.size = (300, 300)


if __name__ == "__main__":
    Application().run()
