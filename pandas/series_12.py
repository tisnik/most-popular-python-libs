#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import numpy as np
import pandas

s1 = pandas.Series(range(1, 7))
s2 = pandas.Series(np.repeat(100, 6))

print(s1 + s2)
print(s1 - s2)
print(s1 * s2)
print(s1 / s2)
print(s1 > s2)
print(s1 < s2)
