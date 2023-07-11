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

from typing import List, Sequence

l1: List[bool] = [True, False]

l1.append(True)
l1.append(False)

print(l1)

l2: Sequence[bool] = [True, False]

l2.append(True)
l2.append(False)

print(l2)
