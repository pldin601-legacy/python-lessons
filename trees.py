__author__ = 'roman'


def partition(num):
    yield [num]
    for x in range(1, num):
        for y in partition(num - x):
            yield [x] + y


def match_pairs(coll, comp):
    if len(coll) < 2:
        return True
    elif comp(coll[0], coll[1]):
        return match_pairs(coll[1::], comp)
    else:
        return False


def compare(x, y):
    return x < y


def find_trees(num):
    for t in partition(num):
        if match_pairs(t, compare):
            print(t)


find_trees(10)