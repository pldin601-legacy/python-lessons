import random
from time import time

gen = lambda count, max: [random.randrange(0, max) for x in range(1, count)]

rostik = lambda a: list(x << 1 for x in a[:len(a) >> 1]) + list(x >> 1 for x in a[len(a) >> 1:])

#m = gen(1000000, 100)

# start = time()
print(list(rostik(gen(10, 100))))
# print("Roman: ", time() - start)

# start = time()
# rostik(m)
# print("Rostik", time() - start)
