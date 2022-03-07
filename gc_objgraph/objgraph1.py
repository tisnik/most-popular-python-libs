"""Grafické zobrazení referencí."""

import objgraph

x = "Foo"
y = x
z = y

# zobrazení referencí vedoucích až na řetězec "Foo"
objgraph.show_refs(z, filename="objgraph1.png")
