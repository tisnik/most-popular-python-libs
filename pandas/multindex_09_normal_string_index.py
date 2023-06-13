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
import numpy as np

sequence2 = ("foo", "bar", "baz", "foo", "bar", "baz", "foo", "bar", "baz", "*")

s = pandas.Series(np.random.randn(10), index=sequence2)
print(s)
print()

print(s["foo"])
print()

print(s["bar"])
print()

print(s["baz"])
print()

print(s["*"])
print()

print(s["other"])
print()
