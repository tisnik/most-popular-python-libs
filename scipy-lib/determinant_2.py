from scipy import linalg

import numpy as np

m = np.zeros((5, 5))
print(m)
print()

det = linalg.det(m)
print("Determinant:" )
print(det)

