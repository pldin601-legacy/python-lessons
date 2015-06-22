__author__ = 'rostik'


def f(a):
    r = range(1, a + 1)
    return set(x for x in r if a % x == 0)


def F(*b):
    return list(f(x) for x in b)


def func(L):
        if len(L) == 1:
                return L

        q = len(L)-1
        x=list(set(L[q])&set(L[q-1]))
        return func(L[:-2]+[x])

print(func(F(1024, 2048)))
