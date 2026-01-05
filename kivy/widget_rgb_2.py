from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.button import Button


class Application(App):

    def build(self):
        layout = GridLayout(cols=5, padding=10, spacing=10)

        slider_red = Slider(min=0, max=100, value=25, orientation="vertical")
        slider_red.fbind("value", self.on_red_slider_change)
        layout.add_widget(slider_red)

        slider_green = Slider(min=0, max=100, value=50, orientation="vertical")
        slider_green.fbind("value", self.on_green_slider_change)
        layout.add_widget(slider_green)

        slider_blue = Slider(min=0, max=100, value=75, orientation="vertical")
        slider_blue.fbind("value", self.on_blue_slider_change)
        layout.add_widget(slider_blue)

        self.label_rgb = Label(text="[size=40pt][b]T\ne\ns\nt[/b][/size]", markup=True)
        layout.add_widget(self.label_rgb)

        button = Button(text="Ok")
        button.on_release=self.stop
        layout.add_widget(button)

        return layout

    def on_red_slider_change(self, instance, value):
        self.red = value / 100.0
        self.change_color()

    def on_green_slider_change(self, instance, value):
        self.green = value / 100.0
        self.change_color()

    def on_blue_slider_change(self, instance, value):
        self.blue = value / 100.0
        self.change_color()

    def change_color(self):
        self.label_rgb.color = (self.red, self.green, self.blue, 1.0)

    def on_start(self):
        self.red = 0.25
        self.green = 0.50
        self.blue = 0.75

        Window.size = (300, 400)
        self.change_color()


if __name__ == "__main__":
    Application().run()
