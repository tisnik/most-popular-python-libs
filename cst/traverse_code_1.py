#!/usr/bin/python
# vim: set fileencoding=utf-8

from libcst import parse_module, CSTVisitor
from libcst.tool import dump


class Visitor(CSTVisitor):
    def __init__(self):
        print("Visitor init")

    def on_visit(self, node):
        print("Visited node: ", node.__class__.__name__)
        return True

    def on_leave(self, node):
        pass


constant = "1 + 2 * 3"

parsed = parse_module(constant)
visitor = Visitor()
parsed.visit(visitor)
