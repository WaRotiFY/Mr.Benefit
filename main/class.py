import sqlite3

conn = sqlite3.connect("server.db")
cur = conn.cursor()

#класс профиля пользователя
class User:
    def __init__(self, name=0, money=0):#заношу личные данные
        self.name = name
        self.money = money
    def getmoney(self):#получаю значение баланса
        User.__init__()
        return self.money
    def setmoney(self, set):#изменяем баланс пользователя
        User.__init__()
        self.money = self.money+set
        sql_update_query = f"""Update user set money = {self.money} where name = {self.name}"""
        cursor.execute(sql_update_query)

#класс для работы с достижениями
class Achievement:
    def __init__(self, name):#заношу все данные о достижениях
        id = (cur.execute(f"SELECT id FROM achivevement WHERE name={name}")).fetchone()
        tasks = (cur.execute(f"SELECT task FROM achivevement WHERE id={id[0]}")).fetchone()
        ismade = (cur.execute(f"SELECT ismade FROM achivevement WHERE id={id[0]}")).fetchone()
        self.tasks = dict(zip(tasks,ismade))
    def addAch(self, task):#добавить достижение в базу данных
        cur.execute("""INSERT INTO achievement VALUES(?,?);""", (task,0))
        conn.commit()
    def  getAch(self):
        Achievement.__init__()
        return self.tasks
