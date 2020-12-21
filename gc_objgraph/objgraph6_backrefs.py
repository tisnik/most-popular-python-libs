"""Grafické zobrazení referencí."""

import objgraph

x = {}
y = {}
z = {}

# cyklické reference N:N
x["->x"] = x
x["->y"] = y
x["->z"] = z

y["->x"] = x
y["->y"] = y
y["->z"] = z

z["->x"] = x
z["->y"] = y
z["->z"] = z

# graf s cyklickými referencemi
objgraph.show_backrefs([x, y, z], filename='objgraph6_backrefs.png')
