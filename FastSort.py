__author__ = 'roman'


def sort(arr: []) -> []:
    if len(arr) == 0:
        return arr
    else:
        pivot = arr[int(len(arr) / 2)]
        return sort(list(filter(lambda x: x < pivot, arr))) + \
               list(filter(lambda x: x == pivot, arr)) + \
               sort(list(filter(lambda x: x > pivot, arr)))


a = [1, 5, 10, 2, 2, 3, 11, 46, -5, 66]

print(sort(a))
