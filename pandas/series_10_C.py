#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import numpy as np
import pandas

s1 = pandas.Series(range(1, 7), ('a', 'b', 'c', 'd', 'e', 'f'))

s1 *= 2

print(s1)
