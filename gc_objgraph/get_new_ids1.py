"""Zjištění konstrukce objektů v paměti."""

import objgraph

x = {}
y = {}

objgraph.get_new_ids()
print()

x["1"] = y

objgraph.get_new_ids()
print()

y["2"] = x

objgraph.get_new_ids()
print()
