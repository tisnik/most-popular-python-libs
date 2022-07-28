#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2022  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky

from pyrsistent import freeze

vector1 = freeze([1, "foo", [1, 2, 3], None])
print(vector1)
print(type(vector1))

vector2 = vector1.append("Five!")
print(vector1)
print(type(vector1))

print(vector2)
print(type(vector2))
