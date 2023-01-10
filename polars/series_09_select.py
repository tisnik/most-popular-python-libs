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

# výběr prvků
print(s[1])
print(s[2, 4, 6])
print(s[2:6])
print(s[1:8:2])
print(s[::2])
print(s[11:0:-1])
print(s[11::-1])
