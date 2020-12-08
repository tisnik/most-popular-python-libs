#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

s = pandas.Series((100.1, 200, 300, None, 400, 500, 600))
print(s.dtypes)
print(s)
print()

s = s.convert_dtypes()
print(s.dtypes)
print(s)
print()
