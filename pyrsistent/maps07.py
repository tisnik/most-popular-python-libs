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

from pyrsistent import pmap

map1 = pmap({1: "first", 2: "second", 3: "third"})
map2 = pmap({3: "3rd", 4: "4th"})

print(map1)
print(map2)

map3 = map1.update(map2)
print(map3)
