#запускать этот файл



from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
import sqlite3
from Class import User


conn = sqlite3.connect("server.db")
cur = conn.cursor()
#Создаю базу данных с профилем пользователя
cur.execute("""CREATE TABLE IF NOT EXISTS user(
            name TEXT,
            money INTEGER);
            """)
conn.commit()
#Создаю базу данных с профилем пользователя
cur.execute("""CREATE TABLE IF NOT EXISTS achievement(
            id INTEGER,
            task TEXT,
            ismade INTEGER);
            """)
conn.commit()



#вид приложения
person=None
class Manager(ScreenManager):
    pass
class StartWindow(MDScreen):
    animation_constant = NumericProperty(40)

    def __init__(self, **kw):
        super().__init__(**kw)
        anim = Animation(animation_constant=10, duration=.6, t='in_out_quad') + Animation(animation_constant=40,
                                                                                          duration=.6, t='in_out_quad')
        anim.repeat = True
        anim.start(self)

class SingIn(MDScreen):
    global person
    def addNick(self):
        person = User(self.ids.text_input.text)
        self.manager.get_screen("menu").ids.lb.text=person.getname()
"""class Update(MDScreen):
    global person
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        cur.execute("SELECT * FROM user")
        prof=cur.fetchall()
        if ( prof!= []):
            person=User(prof[0][0])
            self.manager.get_screen("menu").ids.lb.text=person.getname()

        self.manager.current = 'menu'"""
class MainMenu(MDScreen):
    pass


class mainApp(MDApp):

    def build(self):
        cur.execute("SELECT * FROM user")
        if (cur.fetchall() == []):
            return Builder.load_file('main.kv')
        else:
            return MainMenu()


if __name__ == '__main__':
    mainApp().run()
