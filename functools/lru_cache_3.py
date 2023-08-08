from time import time
from functools import lru_cache

@lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


max_n = 40

for _ in range(10):
    print(fib.cache_info())
    start = time()
    result = fib(max_n)
    end = time()
    print(result, end - start)
