from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.button import Button


class Application(App):
    def build(self):
        layout = GridLayout(cols=2, padding=10, spacing=10)

        # prvni radek mrizky
        label1 = Label(text="I really want to receive spam")
        layout.add_widget(label1)
        ack1 = CheckBox(active=True, size_hint_x=None, width=50)
        layout.add_widget(ack1)

        # druhy radek mrizky
        label2 = Label(text="Share my data with FAANG")
        layout.add_widget(label2)
        ack2 = CheckBox(active=True, size_hint_x=None, width=50)
        layout.add_widget(ack2)

        # treti radek mrizky
        button = Button(text="Ok")
        button.on_release=self.stop
        layout.add_widget(button)

        return layout

    def on_start(self):
        Window.size = (350, 160)


if __name__ == "__main__":
    Application().run()
