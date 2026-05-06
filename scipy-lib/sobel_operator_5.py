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
filtered = ndimage.sobel(input_matrix, axis=0)

print(filtered)

print()

# aplikace filtru
filtered2 = ndimage.sobel(input_matrix, axis=1)

print(filtered2)
