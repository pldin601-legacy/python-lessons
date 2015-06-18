__author__ = 'Roman'

string = "Hello"

def combine(source: str):
    for char in source:
        yield char


for variant in combine(string):
    print(variant)
