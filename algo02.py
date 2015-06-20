__author__ = 'roman'


def group(size, coll):
    return list(coll[n:n+size]
                for n in range(0, len(coll), size))


def apply(numbers):
    return [numbers[0] * 3, numbers[1] * 2]


def flat(coll):
    return [item for lst in coll for item in lst]


def do(numbers):
    return flat(map(apply, group(2, numbers)))


def func(arr):
    return [x * 3 if x % 2 != 0 else x * 2 for x in arr]


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(func(a))
