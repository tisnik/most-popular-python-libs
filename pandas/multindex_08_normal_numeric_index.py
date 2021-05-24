#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas
import numpy as np

sequence1 = range(10)

s = pandas.Series(np.random.randn(10), index=sequence1)
print(s)
print()

print(s[0])
print()

print(s[9])
print()

print(s[10])
print()
