__author__ = 'roman'


def group(size, coll):
    return list(coll[n:n+size]
                for n in range(0, len(coll), size))


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(list(group(4, a)))
