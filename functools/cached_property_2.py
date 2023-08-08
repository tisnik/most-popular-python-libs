from time import time
from functools import cached_property


class FibonacciNumber:
    def __init__(self, n):
        self._n = n

    @cached_property
    def value(self):
        return FibonacciNumber.compute(self._n)

    @staticmethod
    def compute(n):
        if n < 2:
            return n
        return FibonacciNumber.compute(n-1) + FibonacciNumber.compute(n-2)


f = FibonacciNumber(40)

for _ in range(10):
    start = time()
    result = f.value
    end = time()
    print(result, end - start)
