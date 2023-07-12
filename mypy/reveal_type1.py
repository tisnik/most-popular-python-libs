#!/usr/bin/env python3
# vim: set fileencoding=utf-8

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

x = 42
reveal_type(x)

y = "foo"
reveal_type(y)

z = (1, "abc", 3.14, True)
reveal_type(z)

class X():
    pass

w = X()
reveal_type(w)
