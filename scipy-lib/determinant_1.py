from scipy import linalg

import numpy as np

m = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 1]])
print(m)
print()

det = linalg.det(m)
print("Determinant:" )
print(det)

