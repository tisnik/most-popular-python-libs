"""Grafické zobrazení referencí."""

import objgraph

x = {}
y = {}

# objekty z celého jmenného prostoru
objgraph.show_refs(globals(), filename="objgraph9.png")
