from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Box Layout Demo class"""
    def build(self):
        """Build GUI for Box Layout Demo program."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Display greeting to the user."""
        # print('test')
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_greet(self):
        """Reset out label and name input."""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
