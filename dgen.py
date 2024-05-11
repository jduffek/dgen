# dgen.py

import sys
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.config import Config

# Define the layout for the random number generator
class duffgenApp(App):
    def __init__(self, num_digits=2, **kwargs):
        super().__init__(**kwargs)
        self.num_digits = num_digits  # Set the number of digits

    def build(self):
        # Load the root widget defined in the .kv file
        root = Builder.load_file('dgen.kv')
        return root

    def on_start(self):
        # Generate a random number with the specified number of digits
        min_num = 10 ** (self.num_digits - 1)
        max_num = (10 ** self.num_digits) - 1
        random_number = random.randint(min_num, max_num)
        # Access the label widget by its id and update its text
        self.root.ids.random_number_label.text = str(random_number)

    def generate_random_number(self):
        # Generate a random number with the specified number of digits
        min_num = 10 ** (self.num_digits - 1)
        max_num = (10 ** self.num_digits) - 1
        random_number = random.randint(min_num, max_num)
        # Access the label widget by its id and update its text
        self.root.ids.random_number_label.text = str(random_number)


if __name__ == '__main__':
    # Parse command-line arguments
    num_digits = 2
    if len(sys.argv) > 1:
        try:
            num_digits = int(sys.argv[1])
        except ValueError:
            pass

    # Set the size of the window
    Config.set('graphics', 'width', '150')
    Config.set('graphics', 'height', '110')

    # Run the Kivy application with parsed arguments
    duffgenApp(num_digits=num_digits).run()
