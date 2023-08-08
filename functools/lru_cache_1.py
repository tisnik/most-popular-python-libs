from time import time

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


max_n = 40

for _ in range(10):
    start = time()
    result = fib(max_n)
    end = time()
    print(result, end - start)
