"""Grafické zobrazení referencí."""

import objgraph

x = "Foo"
y = [x, "bar"]

objgraph.show_backrefs(y, filename='objgraph2_backrefs.png')
