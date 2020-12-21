"""Zjištění počtu objektů v paměti."""

import objgraph
import queue

x = {}
y = {}

objgraph.show_growth()
print()

x["1"] = y

objgraph.show_growth()
print()

y["2"] = x

objgraph.show_growth()
print()

x = Exception()
y = queue.Queue()
z = queue.LifoQueue()

objgraph.show_growth()
print()
