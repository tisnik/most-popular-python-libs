#!/usr/bin/python
# vim: set fileencoding=utf-8

from libcst import parse_module, CSTVisitor
from libcst.tool import dump


class Visitor(CSTVisitor):
    def __init__(self):
        self.nest_level = 0

    def on_visit(self, node):
        indent = " " * self.nest_level * 2
        print(indent, node.__class__.__name__)
        self.nest_level += 1
        return True

    def on_leave(self, node):
        self.nest_level -= 1


expression = "1 + 2 * 3"

parsed = parse_module(expression)
visitor = Visitor()
parsed.visit(visitor)
