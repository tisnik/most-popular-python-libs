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

from libcst import CSTTransformer, parse_module


class Transformer(CSTTransformer):
    def __init__(self):
        pass

    def on_visit(self, node):
        print(node.__class__.__name__)
        return True

    def leave_Name(self, original_node, updated_node):
        if original_node.value == "foo":
            print("Renaming 'foo' to 'bar'")
            return updated_node.with_changes(value="bar")
        return original_node

    def on_visit_attribute(self, node, attribute):
        print("-> attribute", attribute)

    def on_leave_attribute(self, node, attribute):
        pass


expression = "1 + foo * 3 - 4 / foo"

parsed = parse_module(expression)
transformer = Transformer()
transformed = parsed.visit(transformer)

print()
print("-" * 60)
print(parsed.code)
print(transformed.code)
