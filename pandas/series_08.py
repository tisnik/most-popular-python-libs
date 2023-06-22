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

s = pandas.Series(range(1, 7), ("a", "b", "c", "d", "e", "f"))

print("Series:")
print(s)
print()

print("Index:")
print(s.index)
print()

print("Values:")
print(s.values)
print()

s = s.reindex(["d", "a", "b", "c", "d", "a", "a", "a"])

print("Reindexed:")
print()

print("Series:")
print(s)
print()

print("Index:")
print(s.index)
print()

print("Values:")
print(s.values)
print()
