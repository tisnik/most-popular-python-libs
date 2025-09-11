#!/usr/bin/env python

from functools import reduce

seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(seznam)

y = reduce(lambda x, y: x + y, seznam)
print(y)


def add(x, y):
    print(x, y)
    return x + y


z = reduce(add, seznam)
print(z)
