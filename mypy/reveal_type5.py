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

from typing import Dict, Union

d:Dict[str, Union[int, float, str]] = {}

reveal_type(d)

d["foo"] = 1
d["bar"] = 3.14
d["baz"] = "*"

reveal_type(d)

d[10] = 10
d[42] = "answer"

reveal_type(d)
