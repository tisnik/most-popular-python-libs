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
filtered = ndimage.gaussian_filter(input_matrix, sigma=0.5)

print(filtered)

print()

# aplikace filtru
filtered2 = ndimage.gaussian_filter(input_matrix, sigma=0.7)

print(filtered2)
