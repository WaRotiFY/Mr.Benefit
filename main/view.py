#запускать этот файл



from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from Class import User


class StartWindow(MDScreen):
    animation_constant = NumericProperty(40)

    def __init__(self, **kw):
        super().__init__(**kw)
        anim = Animation(animation_constant=10, duration=.6, t='in_out_quad') + Animation(animation_constant=40,
                                                                                          duration=.6, t='in_out_quad')
        anim.repeat = True
        anim.start(self)

class SingIn(MDScreen):

    def addNick(self):
        print(self.ids.text_input.text)
        person = User(self.ids.text_input.text)

class WindowManage(ScreenManager):
    pass
class mainApp(MDApp):

    def build(self):
        return Builder.load_file('main.kv')


if __name__ == '__main__':
    mainApp().run()
