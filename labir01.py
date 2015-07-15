
lab = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

start = [0, 0]
end = [9, 5]


def find_path(st, dst, l):

    if st[0] == dst[0] and st[1] == dst[1]:
        return True

    x = st[0]
    y = st[1]
    l[y][x] = 1

    if x > 0 and l[y][x - 1] == 0:
        if find_path([x - 1, y], dst, l):
            return True

    if x < len(l[0]) - 1 and l[y][x + 1] == 0:
        if find_path([x + 1, y], dst, l):
            return True

    if y > 0 and l[y - 1][x] == 0:
        if find_path([x, y - 1], dst, l):
            return True

    if y < len(l) - 1 and l[y + 1][x] == 0:
        if find_path([x, y + 1], dst, l):
            return True

    return False


print(find_path(start, end, lab))


