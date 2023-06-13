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

sequence1 = range(10)
sequence2 = ("foo", "bar", "baz", "foo", "bar", "baz", "foo", "bar", "baz", "*")

zipped = zip(sequence1, sequence2)

print("zipped sequences")
print(zipped)
print()

tuples = tuple(zipped)

print("converted to tuples")
print(tuples)
print()

multiindex = pandas.MultiIndex.from_tuples(tuples, names=["first", "second"])

print("multiindex made from tuples")
print(multiindex)
print()

s = pandas.Series(np.random.randn(10), index=multiindex)
print(s)
print()

print(s[0, "foo"])
print(s[0]["foo"])
print()

print(s[0, "other"])
