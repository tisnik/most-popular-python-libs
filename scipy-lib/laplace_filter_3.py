import numpy as np

from scipy import ndimage


input_matrix = np.array([
    [5, 5, 5, 5, 5, 5],
    [5, 0, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 5],
    [5, 5, 5, 5,10, 5],
    [5, 5, 5, 5, 5, 5],
    ])

# aplikace filtru
filtered = ndimage.laplace(input_matrix)

print(filtered)
