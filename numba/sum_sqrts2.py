from numba import jit

import numpy as np


@jit(nopython=True)
def sum_array(array):
    result = 0.
    for x in array:
        result += np.sqrt(x)
    return result


array = np.arange(1, 100000001)
x = 0

for _ in range(100):
    x += sum_array(array)

print(sum_array(array))
