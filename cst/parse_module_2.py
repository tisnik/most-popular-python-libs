#!/usr/bin/python
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from libcst import parse_module
from libcst.tool import dump

expression = "1  + 2"

parsed = parse_module(expression)
print("Parsed:")
print(parsed)

print()

dumped = dump(parsed)
print("Dumped:")
print(dumped)

print()

code = parsed.code
print("Code:")
print(code)
