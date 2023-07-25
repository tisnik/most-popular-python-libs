from functools import reduce


def factorial(n):
    return reduce(lambda a, b: a*b, range(1, n+1), 1)


for n in range(0, 11):
    print(n, factorial(n))
