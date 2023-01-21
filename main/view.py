from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class Container(GridLayout):
    def add_task(self):
        pass


class MyApp(App):
    def build(self):

        return Container()

if __name__ == '__main__':
    MyApp().run()