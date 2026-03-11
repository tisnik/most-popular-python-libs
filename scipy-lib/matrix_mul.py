import numpy as np

m1 = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 1]])
m2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Matrix M1")
print(m1)
print()

print("Matrix M2")
print(m2)
print()

print("M1xM2")
print(m1 @ m2)

