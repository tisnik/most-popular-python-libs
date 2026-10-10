from scipy import linalg

import numpy as np

m = np.array([[0+0j, 1+0j, 0+1j], [1+0j, 1+1j, 1-1j], [0+0j, 1+0j, 1+2j]])
print(m)
print()

inv = linalg.inv(m)
print("Inverse matrix:" )
print(inv)

