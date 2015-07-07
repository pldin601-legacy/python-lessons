__author__ = 'roman'


def concat(*args):

    if len(args) == 0:
        return None

    result = args[0]

    for n in args[1:]:
        result += n

    return result

print(concat("Hello", "World"))
