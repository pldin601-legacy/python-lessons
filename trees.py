__author__ = 'roman'


def partition(num):
    yield [num]
    for x in range(1, num):
        for y in partition(num - x):
            yield [x] + y


def match_pairs(coll, comp):
    if len(coll) < 2:
        return True
    for a in range(len(coll) - 1):
        if not comp(coll[a], coll[a + 1]):
            return False
    return True


def compare(x, y):
    return x < y


def find_trees(num):
    for t in partition(num):
        if match_pairs(t, compare):
            print(t)


find_trees(10)