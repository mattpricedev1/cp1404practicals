from kivy.app import App
from kivy.app import Builder
from kivy.core.window import Window

KM_PER_MILE = 1.609


class MilesConverterApp(App):

    def build(self):
        Window.size = (500, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_conversion(self):
        value = self.get_valid_number()
        result = value * KM_PER_MILE
        # convert result from float to str
        self.root.ids.output_result.text = str(result)

    def handle_increment(self, change):
        value = self.get_valid_number() + change
        self.root.ids.input_miles.text = str(value)

    def get_valid_number(self):
        try:
            # convert value from str to float
            value = int(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
