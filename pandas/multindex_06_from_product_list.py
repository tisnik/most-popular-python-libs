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

sequence1 = list(range(1, 6))
sequence2 = ["foo", "bar", "baz"]

sequences = (sequence1, sequence2)

print("sequences")
print(sequences)
print()

multiindex = pandas.MultiIndex.from_product(sequences, names=["first", "second"])

print("multiindex made from tuples")
print(multiindex)
print()
