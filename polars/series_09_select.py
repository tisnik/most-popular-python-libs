#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2023  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import polars

# vytvoření datové řady
s = polars.Series("sloupec", range(1, 11))

# zobrazíme datovou řadu
print(s)
print()

# podrobnější informace o datové řadě
print("Column type")
print(s.dtype)
print()

# výběr prvků
print(s[1])
print(s[2, 4, 6])
print(s[2:6])
print(s[1:8:2])
print(s[::2])
print(s[11:0:-1])
print(s[11::-1])
