"""Grafické zobrazení referencí."""

import objgraph

x = "Foo"
y = [x, "bar", [x], (x, x), {"x": x}]

objgraph.show_backrefs([x, y], filename="objgraph4_backrefs.png")
