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

    def __add__(self, other):
        return Products(self, other)


class Products(object):
    def __init__(self, *source):
        self.__list = list(source)

    def __add__(self, other):
        new = Products(*self.__list)
        new += other
        return new

    def __iadd__(self, other):
        self.__list.append(other)
        return self

    def calories(self):
        return sum(map(lambda x: x.calories(), self.__list))

    def length(self):
        return len(self.__list)

    def __str__(self):
        return "(List of %d products with sum of %d calories)" % (self.length(), self.calories())

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        for i in self.__list:
            yield i

    def __getitem__(self, item):
        return self.__list.__getitem__(item)

    def __cmp__(self, other):
        return self.calories() - other.calories()

    def __len__(self):
        return self.length()

    def pop(self, i):
        return self.__list.pop(i)


products = Product("Beer", 31) + Product("Chocolate", 45) + \
           Product("Wine", 11) + Product("Pizza", 55) + \
           Product("Sushi", 54) + Product("Tea", 10) + \
           Product("Cake", 35) + Product("Ice", 63) + \
           Product("Orange", 5) + Product("Snickers", 80)


copy = products[::]

print(copy)