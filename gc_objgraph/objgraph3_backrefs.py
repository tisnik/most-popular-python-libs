"""Grafické zobrazení referencí."""

import objgraph

x = "Foo"
y = [x, "bar"]

objgraph.show_backrefs([y], filename="objgraph3_backrefs.png")
