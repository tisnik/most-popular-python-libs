#!/usr/bin/env python3
# vim: set fileencoding=utf-8

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

# výběr prvků na základě filtru
print(s[s > 5])
print(s[s < 5])
print(s[s != 5])
print(s[s %2 == 1])
print(s[s %2 != 1])
