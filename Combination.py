__author__ = 'Roman'

string = "Hello"

def combine(source: str):
    if len(source) == 1:
        yield source
    for i, char in enumerate(source):
        rest = source[:i] + source[i+1:]
        for v in combine(rest):
            yield char + v


for variant in combine(string):
    print(variant)
