#запускать этот файл



from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from сlass import Achievement

main=Achievement()
class intro(GridLayout):
   
   pass 
class Container(GridLayout):
    def add_task(self):
        set=self.task.text
        main.addAch(task=set)


class MyApp(App):
    def build(self):
        if(True):
         return Container()
        else:
         return intro()

if __name__ == '__main__':
    MyApp().run()
