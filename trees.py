__author__ = 'roman'


def partition(num):
    return list(filter(lambda v: match_pairs(v, lambda x, y: x < y),
                       [[num]] + [[x] + y for x in range(1, num) for y in partition(num - x)]))


def match_pairs(coll, comp):
    if len(coll) < 2:
        return True
    elif comp(coll[0], coll[1]):
        return match_pairs(coll[1::], comp)
    else:
        return False


print(len(partition(10)))