from scipy import linalg

import numpy as np

m1 = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 1]])

print("Matrix M")
print(m1)
print()

m2 = linalg.inv(m1)

print("Inverse matrix")
print(m2)
print()

print("M1xM2")
print(m1 @ m2)
