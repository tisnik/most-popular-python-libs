"""Zobrazení počtu referencí na řetězec."""

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

import sys


def foo(ref):
    bar(ref)


def bar(ref):
    print(sys.getrefcount(ref))


# reference na řetězec
x = "Test!"
print(sys.getrefcount(x))

# předání reference
foo(x)
