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
s = polars.Series("sloupec", (1, 2, 3, 4))

# zobrazíme datovou řadu
print(s)
print()

# podrobnější informace o datové řadě
print("Column type")
print(s.dtype)
print()
