#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

s = pandas.Series((100, 200, 300, 400, 500, 600))
print(s.dtypes)
print(s)
print()

s = s.astype('float16')
print(s.dtypes)
print(s)
print()
