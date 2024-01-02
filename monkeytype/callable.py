#!/usr/bin/env python

def foo(x, y, function):
    return function(x, y)


def main():
    print(foo(1, 2, lambda x, y: x+y))
