#!/usr/bin/python
# vim: set fileencoding=utf-8

from libcst import parse_module, CSTVisitor
from libcst import BinaryOperation, Integer, Add, Multiply
from libcst import SimpleWhitespace, TrailingWhitespace, SimpleStatementLine, Newline
from libcst.tool import dump


class Visitor(CSTVisitor):
    def __init__(self):
        self.nest_level = 0

    def on_visit(self, node):
        indent = " " * self.nest_level * 2
        info = node.__class__.__name__
        self.nest_level += 1

        if isinstance(node, SimpleWhitespace) or \
           isinstance(node, TrailingWhitespace) or \
           isinstance(node, SimpleStatementLine) or \
           isinstance(node, Newline):
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


expression = "1 + 2 * 3 + 4 * 5"

parsed = parse_module(expression)
visitor = Visitor()
parsed.visit(visitor)
