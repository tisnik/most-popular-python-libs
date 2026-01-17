# Knihovna Kivy
#
# - GUI aplikace s jediným dialogem
# - načtení definice dialogu popsaného v jazyku Kv
# - dialog je postaven na kontejneru typu StackLayout

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class Application(App):
    def build(self):
        builder = Builder.load_file("stack_layout.kv")
        return builder

    def on_start(self):
        Window.size = (200, 200)


if __name__ == "__main__":
    Application().run()
