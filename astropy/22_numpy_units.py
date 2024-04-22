import numpy as np
from astropy import units as u

a = np.array(range(10)) + 1
print("a = ", a)

t = a * u.second
print("t = ", t)

d = t / t
print("d = ", d)
