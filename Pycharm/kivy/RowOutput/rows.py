from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.recycleview import RecycleView
from kivy.uix.label import Label

class Introduccion(Screen):
    numbers = ObjectProperty()
    number_list = ObjectProperty()

    def Add_ToList(self):
        self.number_list.data.append({'text': str(self.numbers.text)})