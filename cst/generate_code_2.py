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

from libcst import parse_module, CSTTransformer


class Transformer(CSTTransformer):
    def __init__(self):
        self.nest_level = 0

    def on_visit(self, node):
        indent = " " * self.nest_level * 2
        print(indent, node.__class__.__name__)
        self.nest_level += 1
        return True

    def on_leave(self, original_node, updated_node):
        self.nest_level -= 1
        return original_node

    def on_visit_attribute(self, node, attribute):
        indent = " " * (self.nest_level + 1) * 2
        print(indent, "-> attribute", attribute)

    def on_leave_attribute(self, node, attribute):
        pass


expression = "1 + 2 * 3 - 4 / 5"

parsed = parse_module(expression)
transformer = Transformer()
transformed = parsed.visit(transformer)

print()
print("-" * 60)
print(transformed.code)
