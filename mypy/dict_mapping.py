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

from typing import Dict, Mapping

d1:Dict[str, float] = {}

d1["foo"] = 1
d1["bar"] = 3.14
d1["baz"] = 0.0

print(d1)

d2:Mapping[str, float] = {}

d2["foo"] = 1
d2["bar"] = 3.14
d2["baz"] = 0.0

print(d2)
