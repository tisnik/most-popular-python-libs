"""Zjištění konstrukce objektů v paměti."""

#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import objgraph
import queue

objgraph.get_new_ids()


def foo():
    """Foo function called during IDs counting."""
    x = Exception()
    y = queue.Queue()
    z = queue.LifoQueue()
    objgraph.get_new_ids()


foo()
objgraph.get_new_ids()
