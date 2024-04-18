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

import numpy as np
import pandas

# přečtení zdrojových dat
s = pandas.Series(["cat", "dog", np.nan, "rabbit"])

# tisk obsahu původní datové řady
print(s)
print()

# mapování hodnot
s2 = s.map({"cat": "kitten", "dog": "puppy"})

# tisk obsahu nové datové řady
print(s2)
