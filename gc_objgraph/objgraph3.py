"""Grafické zobrazení referencí."""

import objgraph

x = "Foo"
y = [x, "bar"]

# zobrazení referencí na dva řetězce uložené v seznamu
objgraph.show_refs([y], filename="objgraph3.png")
