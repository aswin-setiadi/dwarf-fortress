import functools

# l = list(range(1, 10))
l = [1, 2, 3]
res = functools.reduce(lambda x, y: x + y / len(l), l, 0)
print(res)
# print(sum(range(1, 10)))
a0 = 0 + 1 / 3
a1 = a0 + 2 / 3
a2 = a1 + 3 / 3
print(a2)
