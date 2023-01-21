import sqlite3

conn = sqlite3.connect("server.db")
cur = conn.cursor()

#класс профиля пользователя
class User:
    def __init__(self, name=0, money=0):#заношу личные данные
        self.name = name
        self.money = money
    def getmoney(self):#получаю значение баланса
        return self.money
    def setmoney(self, set):#изменяем баланс пользователя
        self.money = self.money+set

#класс для работы с достижениями
class Achievement:
    def __init__(self, tasks=[-1], ismade=[-1]):#заношу все данные о достижениях
        self.tasks = dict(zip(tasks,ismade))
    def addAch(self, task):#добавить достижение в базу данных
        cur.execute("""INSERT INTO achievement VALUES(?,?);""", (task,0))
        conn.commit()
