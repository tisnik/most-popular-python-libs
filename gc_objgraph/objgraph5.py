"""Grafické zobrazení referencí."""

import objgraph

x = {}
y = {}

# prázdné slovníky
objgraph.show_refs([x, y], filename="objgraph5A.png")

x["1"] = y

# jedna reference
objgraph.show_refs([x, y], filename="objgraph5B.png")

y["2"] = x

# cyklická reference
objgraph.show_refs([x, y], filename="objgraph5C.png")

x["a"] = 10
x["b"] = True
x["c"] = False
x["d"] = None

y["a"] = False
y["b"] = True
y["c"] = False
y["d"] = None

# přidání dalších referencí
objgraph.show_refs([x, y], filename="objgraph5D.png")
