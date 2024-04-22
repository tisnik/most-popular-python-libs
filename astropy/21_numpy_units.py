import numpy as np
from astropy import units as u

a = np.array(range(10)) + 1
print("a = ", a)

t = a * u.second
print("t = ", t)

l = np.array(1.0) * u.meter
print("l = ", l)

v = l / t
print("v = ", v)
