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

def add(a:bool, b:bool) -> bool:
    return a and b

print(add(1, 2))
print(add(1, True))
print(add(1, False))
print(add(True, False))
