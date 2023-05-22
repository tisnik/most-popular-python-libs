from numba import jit
import numpy as np


@jit(nopython=True,nogil=True,parallel=True)
def parallel_sum(a, b):
     return a+b


x = np.arange(0, 1000)
y = np.zeros(1000)
z = parallel_sum(x, y)

print(x)
print(y)
print(z)
