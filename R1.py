__author__ = 'rostik'

import time


def f(a):
    r = range(1, a + 1)
    return set(x for x in r if a % x == 0)


def F(*b):
    return list(f(x) for x in b)


def func(L):
        if len(L) == 1:
                return L[0]

        head = L[0]
        tail = L[1:]

        return head & func(tail)


counter = 0
start = time.clock()
while time.clock() - start < 5:
    func(F(1024, 2048))
    counter += 1

print(counter)
