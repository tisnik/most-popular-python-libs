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

from libcst import (
    Add,
    BinaryOperation,
    CSTVisitor,
    Integer,
    Multiply,
    SimpleWhitespace,
    parse_module,
)


class Visitor(CSTVisitor):
    def __init__(self):
        self.nest_level = 0

    def on_visit(self, node):
        indent = " " * self.nest_level * 2
        info = node.__class__.__name__
        self.nest_level += 1

        if isinstance(node, SimpleWhitespace):
            return True

        if isinstance(node, BinaryOperation):
            info = "Binary operation: " + node.operator.__class__.__name__

        if isinstance(node, Integer):
            info = node.value

        if isinstance(node, Add):
            info = "+"

        if isinstance(node, Multiply):
            info = "*"

        print(indent, info)

        return True

    def on_leave(self, node):
        self.nest_level -= 1


expression = "1 + 2 * 3"

parsed = parse_module(expression)
visitor = Visitor()
parsed.visit(visitor)
