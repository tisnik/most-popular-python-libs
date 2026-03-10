import numpy as np
from scipy import linalg

m = np.zeros((5, 5))
print(m)
print()

inv = linalg.inv(m)
print("Inverse matrix:" )
print(inv)
