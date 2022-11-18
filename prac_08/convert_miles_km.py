from kivy.app import App
from kivy.app import Builder
from kivy.core.window import Window


class ConversionApp(App):
    def build(self):
        Window.size = (500, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root


ConversionApp().run()
