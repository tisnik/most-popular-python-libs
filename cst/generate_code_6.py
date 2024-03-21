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

from difflib import unified_diff

from libcst import CSTTransformer, Divide, Multiply, Name, SimpleWhitespace, parse_module


class BinaryOpReplacer(CSTTransformer):
    def __init__(self):
        pass

    def on_visit(self, node):
        print(node.__class__.__name__)
        return True

    def leave_Multiply(self, original_node, updated_node):
        print("Replacing multiply by divide")
        return Divide()

    def leave_Divide(self, original_node, updated_node):
        print("Replacing divide by multiply")
        return Multiply()

    def on_visit_attribute(self, node, attribute):
        print("-> attribute", attribute)

    def on_leave_attribute(self, node, attribute):
        pass


expression = "1 + 2 * 3 - 4 / 5\n"

parsed = parse_module(expression)
transformer = BinaryOpReplacer()
transformed = parsed.visit(transformer)

print()
print("-" * 60)
print(parsed.code)
print(transformed.code)

diff = "".join(unified_diff(parsed.code.splitlines(1), transformed.code.splitlines(1)))
print(diff)
