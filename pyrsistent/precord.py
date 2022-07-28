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

from pyrsistent import PRecord, field


class XYRecord(PRecord):
    x = field()
    y = field()


record1 = XYRecord(x=1)
print(record1)

record2 = record1.set("y", 42)
print(record2)

record3 = record2.set("z", 0)
print(record3)
