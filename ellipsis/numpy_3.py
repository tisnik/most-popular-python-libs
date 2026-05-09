import numpy as np

a=np.arange(24)
print(a)
print()

b=a.reshape((3, 4, 2))
print(b)
print()

print(b[1, ..., 1])
print()

print(b[2, ..., 0])
print()
