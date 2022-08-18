#!/usr/bin/python
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2022  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import ast
import dis


class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.nest_level = 1

    def visit(self, node):
        indent = " " * self.nest_level * 2
        print(indent, node)
        self.nest_level += 1
        self.generic_visit(node)
        self.nest_level -= 1


tree = ast.parse("print(a+b*(c-d/e)+f)", mode="exec")

visitor = Visitor()
visitor.visit(tree)

print("Compiling")

compiled = compile(tree, filename="<ast>", mode="exec")

print("Decompiling")

dis.dis(compiled)

print("Done")
