import numpy as np
from scipy import linalg

m = np.array([[0+0j, 1+0j, 0+1j], [1+0j, 1+1j, 1-1j], [0+0j, 1+0j, 1+2j]])
print(m)
print()

det = linalg.det(m)
print("Determinant:" )
print(det)

