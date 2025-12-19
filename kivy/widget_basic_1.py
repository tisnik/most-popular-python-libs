from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class Application(App):
    def build(self):
        layout = GridLayout(cols=1, padding=10, spacing=10)

        # prvni radek mrizky
        label1 = Label(text="Basic widgets")
        layout.add_widget(label1)

        # druhy radek mrizky
        label2 = Label()
        layout.add_widget(label2)

        # treti radek mrizky
        button = Button(text="Ok")
        button.on_press=self.stop
        layout.add_widget(button)

        return layout

    def on_start(self):
        Window.size = (400, 180)


if __name__ == "__main__":
    Application().run()
