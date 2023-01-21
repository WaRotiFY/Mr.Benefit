#класс профиля пользователя
class User:
    def __init__(self, name=0, money=0):#заношу личные данные
        self.name = name
        self.money = money
    def getmoney(self):#
        return self.money
    def setmoney(self, set):
        self.money = self.money+set


class Achievement:
    def __init__(self, tasks=[-1], ismade=[-1]):
        self.tasks = dict(zip(tasks,ismade))

