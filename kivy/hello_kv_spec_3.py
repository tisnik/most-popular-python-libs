from kivy.app import App
from kivy.lang import Builder

class TestApp(App):
    def build(self):
        builder = Builder.load_file("TestApp3.kv")
        return builder

application = TestApp()
application.run()
