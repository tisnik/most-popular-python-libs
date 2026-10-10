from scipy import linalg

import numpy as np

m = np.zeros((5, 5))
print(m)
print()

inv = linalg.inv(m)
print("Inverse matrix:" )
print(inv)
