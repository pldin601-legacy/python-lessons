__author__ = 'roman'


from functools import reduce


def sum(x, y):
    return x + y


def prod(x, y):
    return x * y


def merge(x, y):
    return 10 * x + y


def eval(arrItems, arrOps):
    if len(arrItems) - len(arrOps) != 1:
        raise ArithmeticError
    init = arrItems[0]
    for i, el in enumerate(arrItems[1:]):
        init = arrOps[i](init, el)
    return init


array = [1, 2, 3, 4, 5]

action = [sum, prod, merge]

# print(eval(array, action))

