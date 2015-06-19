__author__ = 'Roman'


def is_factor(number: int):
    return lambda factor: number % factor == 0

def factors(number: int):
    return list(filter(is_factor(number), range(1, number + 1)))

def num_factors(number: int):
    return len(factors(number))

def is_simple(number: int) -> bool:
    return num_factors(number) == 2

def simple(limit: int):
    return list(filter(is_simple, range(1, limit + 1)))


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


print(simple_after(531))
