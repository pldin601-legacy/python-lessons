__author__ = 'rostik'


def f(a):
        m = []
        div = list(range(1, a + 1))
        for x in div:
                if a % x == 0:
                        m += [x]
        return m


def F(*b):
    return [f(x) for x in b]


def func(L):
        if len(L) == 1:
                return L

        q = len(L)-1
        x=list(set(L[q])&set(L[q-1]))
        return func(L[:-2]+[x])

print(func(F(1024, 2048)))
