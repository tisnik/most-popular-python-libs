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

s = pandas.Series((100, 200, 300, 400, 500, 600), dtype="O")
print(s.dtypes)
print(s)
print()

s = s.convert_dtypes()
print(s.dtypes)
print(s)
print()
