__author__ = 'Roman'

import math


def is_factor(number: int):
    return lambda factor: number % factor == 0


def factors(number: int):
    f = list(filter(is_factor(number), range(1, int(math.sqrt(number)) + 1)))
    return sorted(f + list(map(lambda x: int(number / x), f)))


def factors_old(number: int):
    return list(filter(is_factor(number), range(1, number + 1)))


def num_factors(number: int):
    return len(factors(number))


def is_simple(number: int) -> bool:
    return num_factors(number) == 2


def simple(limit: int):
    return list(filter(is_simple, range(1, limit + 1)))


def last_simple(number: int):
    return simple(number)[-1]


def next_simple(initial, predicate, calculate):
    while True:
        if predicate(initial) is True:
            return initial
        initial = calculate(initial)


def inc(value: int) -> int:
    return value + 1


def dec(value: int) -> int:
    return value - 1


def simple_after(number: int):
    return next_simple(number + 1, is_simple, inc)


def split(number: int) -> list:
    while number > 0:
        s = last_simple(number)
        number -= s
        yield s


