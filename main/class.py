class User:
    def __init__(self, name=0, money=0):
        self.name = name
        self.money = money
    def getmoney(self):
        return self.money


class Achievement:
    def __init__(self, tasks=[0]):
        self.tasks = tasks
