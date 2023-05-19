from numba import jit

import numpy as np


@jit(nopython=True)
def sum_array(array):
    result = 0
    for i in range(array.shape[0]):
        result += array[i]
    return result


array = np.arange(1, 1001)
print(sum_array(array))
