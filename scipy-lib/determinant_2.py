import numpy as np
from scipy import linalg

m = np.zeros((5, 5))
print(m)
print()

det = linalg.det(m)
print("Determinant:" )
print(det)

