#классы теперь полность связаны с базой данных, тоесть просто импортируйте классы в файл, вызываете его, обязательным аргументом является имя пользователя
#тоесть вы пишите a=User("name") (объявляете класс) и в скобочках указываете имя пользователя, если такого нет, то его заносят в базу
#после объявления доступны команды a.getmoney()-вы получаете баланс пользователя, чье имя было введено тут a=User("name"),
#аналогично a.setmoney(number)-в скобочках указываете число: на сколько надо измеенить баланс, тоесть если вписать -10, то от счета отнимется 10 валюты, просто 10 - это +10 к балансу
#a.getname()-получаем имя пользователя введенное тут a=User("name")
#так же a=Achievement("name") (объявляете класс) и в скобочках указываете имя пользователя,
#советую сначало объявлять a=User("name") и за тем уже n=Achievement(a.getname()) (так правильнее, не предется в ручную отслеживать имя пользователя, так же не будет конфликта с неинициализированным пользователем)
#n.addAch("task")-добавляем в базу данных задания, на место task передать название задания ввиде строки
#n.getAch()-получаем задания ввиде словаря, где ключ - название, а значение - 0 или 1 (0-задание не сделано, 1-задание сделано)
import sqlite3

conn = sqlite3.connect("server.db")
cur = conn.cursor()

#класс профиля пользователя
class User:
    def __init__(self, name):#заношу личные данные
        cur.execute("SELECT name FROM user WHERE name = ?", (name,))
        if cur.fetchone() is None:
            cur.execute("""INSERT INTO user VALUES(?,?);""", (name,0))
            conn.commit()
        profile = cur.execute(f"""SELECT * FROM user WHERE name="{name}"  """).fetchone()
        self.name = profile[0]
        self.money = profile[1]
    def getmoney(self):#получаю значение баланса
        self.__init__(name=(self.name))
        return self.money
    def setmoney(self, set):#изменяем баланс пользователя
        self.__init__(name=(self.name))
        self.money = self.money+set
        sql_update_query = f"""UPDATE user SET money = {self.money} WHERE name = "{self.name}"  """
        cur.execute(sql_update_query)
        conn.commit()
    def getname(self):#получаю имя пользователя
        self.__init__(name=(self.name))
        return self.name

#класс для работы с достижениями
class Achievement:
    def __init__(self, name):#заношу все данные о достижениях
        self.name=name
        id = (cur.execute(f"""SELECT rowid FROM user WHERE name = "{name}" """)).fetchone()
        tasks = (cur.execute(f"""SELECT task FROM achievement WHERE id={id[0]}""")).fetchall()
        ismade = (cur.execute(f"""SELECT ismade FROM achievement WHERE id={id[0]}""")).fetchall()
        self.id=id[0]
        if tasks!=None:
            self.tasks = dict(zip(tasks,ismade))
    def addAch(self, task):#добавить достижение в базу данных
        cur.execute("""INSERT INTO achievement VALUES(?,?,?);""", (self.id, task,0))
        conn.commit()
    def  getAch(self):
        self.__init__(self.name)
        return self.tasks
