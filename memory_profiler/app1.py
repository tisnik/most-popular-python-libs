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

from time import sleep

sleep(2)

x = "*foo*"

sleep(2)

y = ""
for i in range(200000):
    y += x

print(len(y))

sleep(2)

x = 0
y = 0

sleep(2)

x = bytearray(1000000)

sleep(2)

x = 0

sleep(2)
