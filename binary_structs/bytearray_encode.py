"""Uložení řetězce do pole bajtů s volitelných kódováním."""

#
#  (C) Copyright 2025  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#


s = "The quick brown fox jumps over the lazy dog"

x = bytearray(s, "ascii")
print(type(x))
print(x)
print()

y = bytearray(s, "utf-8")
print(type(y))
print(y)
print()

z = bytearray(s, "utf-16-le")
print(type(z))
print(z)
print()

w = bytearray(s, "utf-16-be")
print(type(w))
print(w)
print()

# UTF-8 s BOM, pouziva ho napriklad Notepad a dalsi divne aplikace
q = bytearray(s, "utf-8-sig")
print(type(q))
print(q)
print()

