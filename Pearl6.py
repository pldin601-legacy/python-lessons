__author__ = 'roman'


def represent(arr_items, arr_ops):
    return "".join([str(a) + b for a, b in zip(arr_items, arr_ops + [""])])


def magic(arr_items, length):
    obj_size = len(arr_items)
    depth = obj_size ** length
    for el in range(0, depth):
        acc = list()
        for j in range(0, length):
            acc.append(arr_items[el % obj_size])
            el = int(el / obj_size)
        yield acc


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

actions = [" + ", "*", ""]

for op in magic(actions, len(array) - 1):
    if eval(represent(array, op)) == 101:
        print(represent(array, op))
