#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import polars
import numpy as np

# vytvoření datové řady
s = polars.Series("sloupec", np.arange(10, 11, 0.1))

# zobrazíme datovou řadu
print(s)
print()

# podrobnější informace o datové řadě
print("Column type")
print(s.dtype)
print()
