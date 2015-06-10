dbl = lambda x: x << 1  # x * 2
hlf = lambda x: x >> 1  # x / 2

f = lambda *a: map(dbl, list(a[:hlf(len(a))])) + map(hlf, list(a[hlf(len(a)):]))

print(f(2, 4, 6, 8, 20, 40, 60, 80))
