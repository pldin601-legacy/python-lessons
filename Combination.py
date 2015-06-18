__author__ = 'Roman'

string = "Hello"

def combine(source: str):
    for i, item in enumerate(source):
        yield item

for variant in combine(string):
    print(variant)
