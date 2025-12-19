from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.button import Button


class Application(App):
    def build(self):
        layout = GridLayout(cols=1, padding=10, spacing=10)

        # prvni radek mrizky
        label1 = Label(text="Background color")
        layout.add_widget(label1)

        # druhy radek mrizky
        toggle_button = ToggleButton(text="Toggle")
        toggle_button.background_color=[1.0, 0.4, 0.6, 1]
        layout.add_widget(toggle_button)

        # treti radek mrizky
        button = Button(text="Ok")
        button.background_color=[0.4, 1.0, 0.4, 1]
        button.on_release=self.stop
        layout.add_widget(button)

        return layout

    def on_start(self):
        Window.size = (400, 180)


if __name__ == "__main__":
    Application().run()
