"""Grafické zobrazení referencí."""

import objgraph

x = "Foo"
y = [x, "bar", [x], (x, x), {"x":x}]

# reference u složitějších datových struktur
objgraph.show_refs([x, y], filename='objgraph4.png')
