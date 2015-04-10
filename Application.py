__author__ = 'roman'

from User import User

me = User("Roman", 29)
me.set_money(100)
me.set_oranges(30)

you = User("Rostik", 28)
you.set_oranges(100)
you.set_money(0)

print me.info()
print you.info()

you.sell_oranges(me, 10, 1)
me.sell_oranges(you, 5, 2)

print me.info()
print you.info()

