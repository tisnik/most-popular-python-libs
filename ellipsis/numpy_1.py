import numpy as np

a=np.arange(25)
print(a)
print()

b=a.reshape((5, 5))
print(b)
print()

print(b[2])
print()

print(b[2, ...])
print()

print(b[..., 2])
print()

