__author__ = 'Roman'

import math
import time


def reduce(fn: callable, coll: [], init=None) -> []:
    tmp = iter(coll)
    value = next(tmp) if init is None else init
    for v in tmp:
        value = fn(value, v)
    return value


def calculate_fractions(number: int):
    def is_fraction(n: int) -> bool:
        return number % n == 0

    def divide(n: int) -> int:
        return int(number / n)

    tmp = list(filter(is_fraction, range(1, int(math.sqrt(number)) + 1)))

    return set(tmp + list(map(divide, tmp)))


def calc_mutual_fractions(*n: int) -> set:
    def intersect(x: set, y: set) -> set:
        return x & y

    return reduce(intersect, map(calculate_fractions, n))


counter = 0
start = time.clock()
while time.clock() - start < 5:
    calc_mutual_fractions(1024, 2048)
    counter += 1

print(calc_mutual_fractions(1024, 2048))
print(counter)

