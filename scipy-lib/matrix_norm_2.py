import numpy as np
from scipy import linalg

m1 = np.array([[0, 1], [1, 0]])
print("Matrix M1")
print(m1)
print()

n = linalg.norm(m1, ord=2)
print("Norm (max):", n)

n = linalg.norm(m1, ord=-2)
print("Norm (min):", n)
