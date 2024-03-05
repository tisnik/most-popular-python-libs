#!/usr/bin/python
# vim: set fileencoding=utf-8

from libcst import parse_module, CSTVisitor
from libcst import BinaryOperation, Integer, Add, Multiply
from libcst.tool import dump


class Visitor(CSTVisitor):
    def __init__(self):
        self.nest_level = 0

    def on_visit(self, node):
        indent = " " * self.nest_level * 2
        info = node.__class__.__name__

        if isinstance(node, BinaryOperation):
            info = "Binary operation: " + node.operator.__class__.__name__

        if isinstance(node, Integer):
            info = node.value

        if isinstance(node, Add):
            info = "+"

        if isinstance(node, Multiply):
            info = "*"

        print(indent, info)

        self.nest_level += 1
        return True

    def on_leave(self, node):
        self.nest_level -= 1


constant = "1 + 2 * 3"

parsed = parse_module(constant)
visitor = Visitor()
parsed.visit(visitor)
