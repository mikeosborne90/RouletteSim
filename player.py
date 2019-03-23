class player:
    def __init__(self, money):
        self.money = money

    def getMoney(self):
        return self.money

    def setMoney(self, money):
        self.money = money

    def addToMoney(self, amount):
        self.money += amount

    def removeFromMoney(self, amount):
        self.money -= amount