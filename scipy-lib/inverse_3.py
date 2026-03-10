import numpy as np
from scipy import linalg

m = np.array([[1, -3], [2, -6]])
print(m)
print()

inv = linalg.inv(m)
print("Inverse matrix:" )
print(inv)

