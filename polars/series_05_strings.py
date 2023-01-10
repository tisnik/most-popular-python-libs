#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import polars

# vytvoření datové řady
s = polars.Series("sloupec", ("foo", "bar", "baz"))

# zobrazíme datovou řadu
print(s)
print()

# podrobnější informace o datové řadě
print("Column type")
print(s.dtype)
print()
