import numpy as np
from scipy import linalg

m = np.array([[1, -3], [2, -6]])
print(m)
print()

det = linalg.det(m)
print("Determinant:" )
print(det)

