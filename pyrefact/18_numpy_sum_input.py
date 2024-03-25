import numpy as np

a = np.random.random((10, 10))

s = 0
for i in a:
    s += i

print(s)
