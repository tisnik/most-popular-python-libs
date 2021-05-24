#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import numpy as np
import pandas

s1 = pandas.Series((1, 2, None, 4, 5, 6), ('a', 'b', 'c', 'd', 'e', 'f'))

print(s1 > 3)
print(s1 < 3)
print(s1 % 2 == 0)
