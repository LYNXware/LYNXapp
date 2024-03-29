print('screen_help.py')

from kivy.uix.boxlayout import BoxLayout
from py_files import __version__
import webbrowser


class HelpScreenCustom(BoxLayout):
    version = f'LYNX app - Version {__version__}'

    def open_link_tutorial(self):
        webbrowser.open('https://www.lynxware.org/tutorials')

    def open_link_contact(self):
        webbrowser.open('https://www.lynxware.org/contact')

    def open_link_shop(self):
        webbrowser.open('https://lynxware.shop/pages/merchandise')