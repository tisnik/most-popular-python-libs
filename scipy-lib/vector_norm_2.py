import numpy as np
from scipy import linalg

v = np.array([0, 1, 2, 3, 0])
print("Vector:", v)

n = linalg.norm(v)
print("Default norm: ", n)

n = linalg.norm(v, ord=float('inf'))
print("Norm for inf: ", n)

n = linalg.norm(v, ord=float('-inf'))
print("Norm for -inf:", n)

n = linalg.norm(v, ord=0)
print("Norm for 0:   ", n)
