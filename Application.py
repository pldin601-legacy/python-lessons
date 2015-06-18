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


# Maximum calories per eating
threshold = 100

# Available meal on a kitchen
products = [
    Product("Beer", 31), Product("Chocolate", 45),
    Product("Wine", 11), Product("Pizza", 55),
    Product("Sushi", 54), Product("Tea", 10),
    Product("Cake", 35), Product("Ice", 63),
    Product("Orange", 5), Product("Snickers", 80),
    Product("Meat", 89), Product("Apple", 42),
    Product("Orange", 5), Product("Snickers", 80),
    Product("Meat", 89), Product("Apple", 42),
    Product("Cherry", 38), Product("Cheese", 29),
    Product("Water", 1), Product("Bread", 42)
]


# Copy list to other list excepting object
def ignore(items: list, i) -> list:
    return list(item for item in items if i != item)


# Count calories in food list
def calories(items: list) -> int:
    return sum(map(lambda x: x.calories(), items))


# Generates combinations of available food
def combine(items: list, other: list, threshold: int):
    result = list()
    result.append(other)
    for char in items:
        rest = ignore(items, char)
        new = other + list([char])
        if calories(new) > threshold:
            result.append(other)
            return result
        else:
            result += combine(rest, new, threshold)
    return result


# Fetches portion of meal from kitchen
def fetch(items: list) -> list:
    combinations = combine(items, list(), 100)
    combinations.sort(key=lambda x: calories(x), reverse=True)
    combination = (lambda x: x[0] if x else None)(combinations)
    for item in combination:
        items.remove(item)
    return combination


# Business logic
while True:
    if len(products) == 0:
        print("The kitchen is empty. Nothing more to eat. Bye!")
        break

    print("Food on a kitchen: ", products)

    ans = input("Do you want some food? (y/n)").lower()

    if ans == "n":
        print("Ok, bye!")
        break

    eat = fetch(products)

    if eat is not None:
        print("You ate: ", eat)
        print("Total calories: ", calories(eat))

    print("")
