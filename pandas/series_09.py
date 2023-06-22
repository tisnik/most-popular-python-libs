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

print("sum", s.sum(), sep="\t")
print("prod", s.prod(), sep="\t")
print("min", s.min(), sep="\t")
print("max", s.max(), sep="\t")
print("median", s.median(), sep="\t")
print("std", s.std(), sep="\t")
print("var", s.var(), sep="\t")
print("quantile", s.quantile(0.01), sep="\t")
