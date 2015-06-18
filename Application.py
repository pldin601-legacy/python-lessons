import time

# Class that represents food object
class Product(object):
    def __init__(self, name, calories):
        self.__name = name
        self.__calories = calories

    def name(self):
        return self.__name

    def calories(self):
        return self.__calories

    def __str__(self):
        return "(%s, %d calories)" % (self.name(), self.calories())

    def __repr__(self):
        return self.__str__()


# Class that represents shelf on a kitchen
class Shelf(object):
    def __init__(self):
        self.__list = list()

    def __iadd__(self, other):
        self.__list.append(other)
        return self

    def __getitem__(self, item):
        return self.__list.__getitem__(item)

    def calories(self):
        return sum(map(lambda x: x.calories(), self.__list))

    def products(self):
        return self.__list[::]

    def __str__(self):
        return str(self.__list)

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.__list)


# Class that represents kitchen object
class Kitchen(object):
    def __init__(self, size=100, *items):
        self.__size = size
        self.__shelves = list()
        for item in items:
            self += item

    def __iadd__(self, other: Product):
        for shelf in self.__shelves:
            if other.calories() + shelf.calories() <= self.__size:
                shelf += other
                return self

        s = Shelf()
        s += other

        self.__shelves.append(s)
        self.__shelves.sort(key=lambda x: x.calories(), reverse=True)

        return self

    def __len__(self):
        return len(self.__shelves)

    def fetch(self):
        if len(self.__shelves):
            return self.__shelves.pop(0)

    def __str__(self):
        return str(self.__shelves)

    def __repr__(self):
        return self.__str__()


# Maximum calories per eating
threshold = 100

# Available meal on a kitchen
kitchen = Kitchen(threshold,
    Product("Beer", 31), Product("Chocolate", 45),
    Product("Wine", 11), Product("Pizza", 55),
    Product("Sushi", 54), Product("Tea", 10),
    Product("Cake", 35), Product("Ice", 63),
    Product("Orange", 5), Product("Snickers", 80),
    Product("Meat", 89), Product("Apple", 42),
    Product("Orange", 5), Product("Snickers", 80),
    Product("Meat", 89), Product("Apple", 42),
    Product("Cherry", 38), Product("Cheese", 29),
    Product("Wine", 11), Product("Pizza", 55),
    Product("Sushi", 54), Product("Tea", 10),
    Product("Cake", 35), Product("Ice", 63),
    Product("Orange", 5), Product("Snickers", 80),
    Product("Meat", 89), Product("Apple", 42),
    Product("Orange", 5), Product("Snickers", 80),
    Product("Meat", 89), Product("Apple", 42),
    Product("Orange", 5), Product("Snickers", 80),
    Product("Meat", 89), Product("Apple", 42),
    Product("Cherry", 38), Product("Cheese", 29),
    Product("Water", 1), Product("Bread", 42)
)

# Business logic
while True:
    if len(kitchen) == 0:
        print("The kitchen is empty. Nothing more to eat. Bye!")
        break

    print("Food on a kitchen: ", kitchen)

    ans = input("Do you want some food? (y/n)").lower()

    if ans == "n":
        print("Ok, bye!")
        break

    start = time.time()
    eat = kitchen.fetch()
    end = time.time()

    if eat is not None:
        print("You ate: ", eat.products())
        print("Total calories: ", eat.calories())
        print("Time: ", str(end - start))

    print("")
