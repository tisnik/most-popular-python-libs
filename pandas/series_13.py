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

s1 = pandas.Series(range(1, 7))
s2 = pandas.Series(range(50))

print(s1[s1 < 3])
print(s1[s1 > 3])

print(s2[s2 % 2 == 0])
print(s2[s2 % 2 != 0])

print(s2[s2 % 3 == 0])
