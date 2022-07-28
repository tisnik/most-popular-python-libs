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

from pyrsistent import pdeque, v

vec = v("foo", "bar", "baz")
deque1 = pdeque(vec)

deque2 = deque1.reverse()
print(deque2)

deque3 = deque1.rotate(1)
print(deque3)
