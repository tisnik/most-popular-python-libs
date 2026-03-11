import numpy as np
from scipy import linalg

m = np.array([[0+1j, 0-3j], [0+2j, 0-6j]])
print(m)
print()

det = linalg.det(m)
print("Determinant:" )
print(det)

