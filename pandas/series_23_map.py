#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas
import numpy as np

# přečtení zdrojových dat
s = pandas.Series(["cat", "dog", np.nan, "rabbit"])

# tisk obsahu původní datové řady
print(s)
print()

mapping = {"cat": "kitten", "dog": "puppy"}

# mapování hodnot
s2 = s.map(mapping)

# tisk obsahu nové datové řady
print(s2)
