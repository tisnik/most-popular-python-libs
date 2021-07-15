"""Grafické zobrazení referencí."""

import objgraph

x = {}
y = {}

# reference mezi objekty
objgraph.show_backrefs(globals(), filename='objgraph9_backrefs.png')
