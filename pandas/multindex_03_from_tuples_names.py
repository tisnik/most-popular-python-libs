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

sequence1 = range(10)
sequence2 = ["foo", "bar", "baz", "foo", "bar", "baz", "foo", "bar", "baz", "*"]

zipped = zip(sequence1, sequence2)

print("zipped sequences")
print(zipped)
print()

lst = list(list(x) for x in zipped)

print("converted to list")
print(lst)
print()

multiindex = pandas.MultiIndex.from_tuples(lst, names=["first", "second"])

print("multiindex made from tuples")
print(multiindex)
print()
