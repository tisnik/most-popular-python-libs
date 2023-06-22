#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import pandas
from collections import OrderedDict

input_data = OrderedDict()

input_data["f"] = 6
input_data["e"] = 5
input_data["d"] = 4
input_data["c"] = 3
input_data["b"] = 2
input_data["a"] = 1

print("Input data:")
print(input_data)
print()

s = pandas.Series(input_data)

print("Series:")
print(s)
print()

print("Index:")
print(s.index)
print()

print("Values:")
print(s.values)
print()
