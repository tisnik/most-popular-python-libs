from functools import reduce

x = range(1, 101)

print(x)

y = reduce(lambda a, b: a + b, x)
print(y)
