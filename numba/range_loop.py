from numba import jit
import numpy as np

@jit(nopython=True)
def range_sum(A):
    sum = 0
    for i in range(A.shape[0]):
        sum += A[i]
    return sum


a = range_sum(np.arange(10000))
print(a)
