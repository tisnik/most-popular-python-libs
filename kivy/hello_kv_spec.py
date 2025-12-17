from kivy.app import App
from kivy.lang import Builder

class TestApp(App):
    def build(self):
        builder = Builder.load_file("TestApp.kv")
        return builder

application = TestApp()
application.run()
