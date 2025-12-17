from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

class TestApp(App):

    def build(self):
        return Label(text="Hello World")

    def on_start(self):
        Window.clearcolor = (0.0, 0.5, 0.5, 1.0)

TestApp().run()
