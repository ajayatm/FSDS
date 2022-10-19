from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        self.layout = GridLayout(cols=2, row_force_default=True, row_default_height=40,
                            spacing=10,padding=20)
        self.weight = TextInput(text='Enter directory path in the next field')
        self.height = TextInput()
        submit = Button(text='Submit', on_press=self.submit)
        self.layout.add_widget(self.weight)
        self.layout.add_widget(self.height)
        self.layout.add_widget(submit)
        return self.layout

    def submit(self,obj):
        q = Label(text="Merged PDF available in your directory")
        self.layout.add_widget(q)

MainApp().run()