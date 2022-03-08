"""Grafické zobrazení referencí."""

import objgraph

x = {}
y = {}

# prázdné slovníky
objgraph.show_backrefs([x, y], filename="objgraph5A_backrefs.png")

x["1"] = y

# jedna reference
objgraph.show_backrefs([x, y], filename="objgraph5B_backrefs.png")

y["2"] = x

# cyklická reference
objgraph.show_backrefs([x, y], filename="objgraph5C_backrefs.png")

x["a"] = 10
x["b"] = True
x["c"] = False
x["d"] = None

y["a"] = False
y["b"] = True
y["c"] = False
y["d"] = None

# přidání dalších referencí
objgraph.show_backrefs([x, y], filename="objgraph5D_backrefs.png")
