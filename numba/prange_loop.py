import numpy as np
from numba import jit, prange


@jit(nopython=True, parallel=True)
def prange_sum(A):
    sum = 0
    for i in prange(A.shape[0]):
        sum += A[i]
    return sum


a = prange_sum(np.arange(10000))
print(a)
