#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas
import numpy

s = pandas.Series((100, 200, 300, numpy.nan, 400, 500, 600))
print(s.dtypes)
print(s)
print()

s = s.convert_dtypes()
print(s.dtypes)
print(s)
print()
