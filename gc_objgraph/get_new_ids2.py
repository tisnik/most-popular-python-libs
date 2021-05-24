"""Zjištění konstrukce objektů v paměti."""

import objgraph
import queue

objgraph.get_new_ids()


def foo():
    x = Exception()
    y = queue.Queue()
    z = queue.LifoQueue()
    objgraph.get_new_ids()


foo()
objgraph.get_new_ids()
