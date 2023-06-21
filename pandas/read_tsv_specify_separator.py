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

"""Reading TSV file that contains column with various values with custom separator."""

import pandas

# separator/delimiter specification
df = pandas.read_csv("tiobe.tsv", sep="\t")

print("Data frame")
print("---------------------------")
print(df)
print()

print("Column types")
print("---------------------------")
print(df.dtypes)
