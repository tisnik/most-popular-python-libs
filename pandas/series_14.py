#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

s1 = pandas.Series(range(1, 7))
s2 = pandas.Series(range(-3, 3))

print(s1[s2 >= 0])
print(s1[s2 < 0])
print(s1[s2 != 0])
