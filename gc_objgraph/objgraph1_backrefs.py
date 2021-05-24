"""Grafické zobrazení referencí."""

import objgraph

x = "Foo"
y = x
z = y

# zobrazení referencí na řetězec "Foo"
objgraph.show_backrefs(x, filename='objgraph1_backrefs.png')
