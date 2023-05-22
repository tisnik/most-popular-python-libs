import time

from numba import jit
import numpy as np


def regular_sum(a, b):
     return a+b


@jit(nopython=True)
def sequential_sum(a, b):
     return a+b


@jit(nopython=True,nogil=True,parallel=True)
def parallel_sum(a, b):
     return a+b


N = 100000

x = np.arange(0, N)
y = np.zeros(N)

print("Let's start")

z = regular_sum(x, y)
z = sequential_sum(x, y)
z = parallel_sum(x, y)

MAX = 100000

print("Compiled")

t1 = time.time()
for _ in range(MAX):
    z = regular_sum(x, y)
t2 = time.time()
print(t2-t1)

t1 = time.time()
for _ in range(MAX):
    z = sequential_sum(x, y)
t2 = time.time()
print(t2-t1)

t1 = time.time()
for _ in range(MAX):
    z = parallel_sum(x, y)
t2 = time.time()
print(t2-t1)
