from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class Application(App):
    def build(self):
        builder = Builder.load_file("box_layout.kv")
        return builder

    def on_start(self):
        Window.size = (400, 300)


if __name__ == "__main__":
    Application().run()
