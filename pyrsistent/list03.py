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

list1 = []

list2 = [1, "foo", (1, 2, 3), list1]
print(list2)
print(type(list2))

list1.append(1)
print(list2)
print(type(list2))

list1.append(2)
print(list2)
print(type(list2))

list1 = []
print(list2)
print(type(list2))
