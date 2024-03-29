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

from pyrsistent import pbag

bag1 = pbag(["foo", "bar", "baz"])

print(bag1)

lst = list(bag1)
print(lst)

bag2 = bag1 + pbag(["baz", "alpha", "omega"])

print(bag2)
