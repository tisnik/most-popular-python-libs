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

    def visit(self, node):
        indent = " " * self.nest_level * 2
        print(indent, node2string(node))
        self.nest_level += 1
        self.generic_visit(node)
        self.nest_level -= 1


def node2string(node):
    t = type(node)
    if t == ast.Constant:
        return "Constant: {}".format(node.value)
    elif t == ast.Name:
        return "Variable: {}".format(node.id)
    elif t == ast.Expr:
        return "Expression:"
    elif t == ast.BinOp:
        return "Binary operation"
    elif t == ast.Add:
        return "Operator: +"
    elif t == ast.Sub:
        return "Operator: -"
    elif t == ast.Mult:
        return "Operator: *"
    elif t == ast.Div:
        return "Operator: /"
    return ""


tree = ast.parse("a+2*(1-b/4)+c")

visitor = Visitor()
visitor.visit(tree)
