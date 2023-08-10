#
#  (C) Copyright 2023  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from functools import partialmethod


class Foo:
    def __init__(self):
        self._enabled = False

    def set_enabled(self, state):
        self._enabled = state

    enable = partialmethod(set_enabled, True)
    disable = partialmethod(set_enabled, False)

    def __str__(self):
        return "Foo that is " + ("enabled" if self._enabled else "disabled")


foo = Foo()
print(foo)

foo.enable()
print(foo)

foo.disable()
print(foo)
