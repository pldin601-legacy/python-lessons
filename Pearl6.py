__author__ = 'roman'


def represent(arr_items, arr_ops):
    if len(arr_items) - len(list(arr_ops)) != 1:
        raise ArithmeticError
    if len(arr_items) == 0:
        raise ArithmeticError
    init = str(arr_items[0])
    for i, el in enumerate(arr_items[1:]):
        init = init + arr_ops[i] + str(el)
    return init


def magic(arr_items, length):
    obj_size = len(arr_items)
    depth = obj_size ** length
    for el in range(0, depth):
        n = el
        acc = list()
        for j in range(0, length):
            acc.append(arr_items[n % obj_size])
            n = int(n / obj_size)
        yield acc


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

actions = [" + ", "*", ""]

for op in magic(actions, len(array) - 1):
    if eval(represent(array, op)) == 101:
        print(represent(array, op))
