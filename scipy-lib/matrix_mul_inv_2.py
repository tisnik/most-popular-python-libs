import numpy as np
from scipy import linalg

m1 = np.array([[0+0j, 1+0j, 0+1j], [1+0j, 1+1j, 1-1j], [0+0j, 1+0j, 1+2j]])

print("Matrix M")
print(m1)
print()

m2 = linalg.inv(m1)

print("Inverse matrix")
print(m2)
print()

print("M1xM2")
print(m1 @ m2)
