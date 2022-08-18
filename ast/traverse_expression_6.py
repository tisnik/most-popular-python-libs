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


class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.nest_level = 1

    def visit_Constant(self, node):
        indent = " " * self.nest_level * 2
        print("{}Constant: {}".format(indent, node.value))
        self.nest_level += 1
        self.generic_visit(node)
        self.nest_level -= 1

    def visit_Name(self, node):
        indent = " " * self.nest_level * 2
        print("{}Variable: {}".format(indent, node.id))
        self.nest_level += 1
        self.generic_visit(node)
        self.nest_level -= 1

    def visit_Expr(self, node):
        indent = " " * self.nest_level * 2
        print("{}Expression:".format(indent))
        self.nest_level += 1
        self.generic_visit(node)
        self.nest_level -= 1

    def visit_BinOp(self, node):
        indent = " " * self.nest_level * 2
        print("{}Binary operator:".format(indent))
        self.nest_level += 1
        self.generic_visit(node)
        self.nest_level -= 1

    def visit_Add(self, node):
        indent = " " * self.nest_level * 2
        print("{}+".format(indent))
        self.nest_level += 1
        self.generic_visit(node)
        self.nest_level -= 1

    def visit_Sub(self, node):
        indent = " " * self.nest_level * 2
        print("{}-".format(indent))
        self.nest_level += 1
        self.generic_visit(node)
        self.nest_level -= 1

    def visit_Mult(self, node):
        indent = " " * self.nest_level * 2
        print("{}*".format(indent))
        self.nest_level += 1
        self.generic_visit(node)
        self.nest_level -= 1

    def visit_Div(self, node):
        indent = " " * self.nest_level * 2
        print("{}/".format(indent))
        self.nest_level += 1
        self.generic_visit(node)
        self.nest_level -= 1


tree = ast.parse("a+2*(1-b/4)+c")

visitor = Visitor()
visitor.visit(tree)
