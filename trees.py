__author__ = 'roman'


def partition(num):
    yield [num]
    for x in range(1, num):
        for y in partition(num - x):
            yield [x] + y


def match_pairs(coll):
    if len(coll) < 2:
        return True
    for a in range(len(coll) - 1):
        if coll[a] >= coll[a + 1]:
            return False
    return True


def match_alt(coll):
    return all(x < y for x, y in zip(coll, coll[1::]))


def find_trees(num):
    for t in partition(num):
        if match_alt(t):
            print(t)


find_trees(14)
