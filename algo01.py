__author__ = 'roman'


def sub(a, b):
    return a - b


def add(a, b):
    return a + b


def enc():
    init = 0

    def inner(number: int):
        nonlocal init
        s = sub(number, init)
        init = number
        return s
    return inner


def dec():
    init = 0

    def inner(number: int):
        nonlocal init
        init = add(number, init)
        return init
    return inner


numbers = [1, 5, 8, 1, 10, -12, 44, 32, 33, 34, 67, -10]
encoded = list(map(enc(), numbers))
decoded = list(map(dec(), encoded))


print(numbers)
print(encoded)
print(decoded)
