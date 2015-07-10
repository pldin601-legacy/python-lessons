__author__ = 'roman'


def partition(num):
    return [[num]] + [[x] + y for x in range(1, num)
                      for y in partition(num - x)]


def rec_range(gen_min, gen_max, step=1):
    print(gen_min)
    if gen_min + step < gen_max:
        rec_range(gen_min + step, gen_max)


def trees(total, need):
    max_step = int(total / need) + 1
    width = lambda step, count: (count - 1) * step + 1
    inclusions = lambda step: total - width(step, need) + 1
    return sum(inclusions(s) for s in range(1, max_step))


print(trees(6, 3))
