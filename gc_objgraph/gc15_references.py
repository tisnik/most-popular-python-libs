"""Example that retrieves and prints reference counts."""

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

import gc
import sys
import pprint


def foo(ref):
    """Call function bar during test."""
    bar(ref)


def bar(ref):
    """Retrieve and print reference counts."""
    print(sys.getrefcount(ref))
    pprint.pprint(len(gc.get_referrers(ref)))
    pprint.pprint(gc.get_referrers(ref))


x = "Test!"
pprint.pprint(gc.get_referrers(x))
print()

foo(x)
