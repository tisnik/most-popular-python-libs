"""Grafické zobrazení referencí."""

import objgraph

x = "Foo"
y = [x, "bar"]

# zobrazení referencí ze seznamu y
objgraph.show_refs(y, filename="objgraph2.png")
