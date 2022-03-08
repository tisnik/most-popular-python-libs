"""Grafické zobrazení referencí."""

import objgraph

a = {}
b = {}
c = {}
d = {}
e = {}
f = {}

a["next"] = b
b["next"] = c
c["next"] = d
d["next"] = e
e["next"] = f
f["next"] = a

# cyklické reference mezi objekty
objgraph.show_backrefs([a, b, c, d, e, f], filename="objgraph8_backrefs.png")
