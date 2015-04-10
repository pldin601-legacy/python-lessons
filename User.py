__author__ = 'roman'


class User:
    _name = None
    _age = None
    _money = 0
    _oranges = 0

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def set_money(self, how_many):
        self._money = how_many

    def set_oranges(self, how_many):
        self._oranges = how_many

    def info(self):
        return "User " + self._name \
               + " is " + str(self._age) + " years old and has " \
               + str(self._oranges) + " oranges and $ " + str(self._money)

    def sell_oranges(self, that, count, cost):
        summ = cost * count
        if that._money < summ:
            print that._name + " has no enough money"
            return
        if self._oranges < count:
            print self._name + " has no enough oranges"
            return
        if cost < 0 or count < 0:
            print "Cost and count must be positive numbers"
            return
        that._money -= summ
        self._oranges -= count
        self._money += summ
        that._oranges += count
