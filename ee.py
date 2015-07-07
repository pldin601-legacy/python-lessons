__author__ = 'roman'


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for n in fibonacci():
    print(n)


