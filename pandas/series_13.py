#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import numpy as np
import pandas

s1 = pandas.Series(range(1, 7))
s2 = pandas.Series(range(50))

print(s1[s1<3])
print(s1[s1>3])

print(s2[s2 % 2 == 0])
print(s2[s2 % 2 != 0])

print(s2[s2 % 3 == 0])
