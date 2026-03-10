import numpy as np
from scipy import linalg

m = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 1]])
print(m)
print()

inv = linalg.inv(m)
print("Inverse matrix:" )
print(inv)

