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


class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.nest_level = 0

    def visit_Module(self, node):
        indent = " " * self.nest_level * 2
        print("{}module begin:".format(indent, node.__dict__))
        self.nest_level += 1
        self.generic_visit(node)
        self.nest_level -= 1
        print("{}module end".format(indent))

    def visit_ClassDef(self, node):
        indent = " " * self.nest_level * 2
        print("{}class {}:".format(indent, node.name))
        self.nest_level += 1
        self.generic_visit(node)
        self.nest_level -= 1

    def visit_For(self, node):
        indent = " " * self.nest_level * 2
        iterator = node.iter
        if type(iterator) == ast.Name:
            iterator = iterator.id
        elif type(iterator) == ast.Call:
            iterator = "call()"

        print("{}for {} in {}:".format(indent, node.target.id, iterator))
        self.nest_level += 1
        self.generic_visit(node)
        self.nest_level -= 1

    def visit_FunctionDef(self, node):
        indent = " " * self.nest_level * 2
        print("{}def {}:".format(indent, node.name))
        self.nest_level += 1
        self.generic_visit(node)
        self.nest_level -= 1


with open("sprites.py") as fin:
    code = fin.read()
    tree = ast.parse(code)
    visitor = Visitor()
    visitor.visit(tree)
