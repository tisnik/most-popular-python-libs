from scipy import linalg

import numpy as np

m1 = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
print("Matrix M1")
print(m1)
print()

n = linalg.norm(m1, ord=None)
print("Norm (Frobenius):", n)
