import numpy as np
from scipy import linalg

m1 = np.array([[-3, 5, 7], [2, 6, 4], [0, 2, 8]])
print("Matrix M1")
print(m1)
print()

n = linalg.norm(m1, ord=1)
print("Norm (max):", n)

n = linalg.norm(m1, ord=-1)
print("Norm (min):", n)
