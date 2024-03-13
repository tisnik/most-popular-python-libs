#!/usr/bin/python
# vim: set fileencoding=utf-8

from libcst import parse_module, CSTTransformer
from libcst import SimpleWhitespace, Name
from difflib import unified_diff


class SymbolRenamer(CSTTransformer):
    def __init__(self, orig_name, new_name):
        self.orig_name = orig_name
        self.new_name = new_name

    def on_visit(self, node):
        print(node.__class__.__name__)
        return True

    def leave_Name(self, original_node, updated_node):
        if original_node.value == self.orig_name:
            print(f"Renaming '{self.orig_name}' to '{self.new_name}'")
            return updated_node.with_changes(value=self.new_name)
        return original_node

    def on_visit_attribute(self, node, attribute):
        print("-> attribute", attribute)

    def on_leave_attribute(self, node, attribute):
        pass


expression = "1 + foo * 3 - 4 / bar\n"

parsed = parse_module(expression)
transformer = SymbolRenamer("foo", "baz")
transformed = parsed.visit(transformer)

print()
print("-" * 60)
print(parsed.code)
print(transformed.code)

diff = "".join(unified_diff(parsed.code.splitlines(1), transformed.code.splitlines(1)))
print(diff)
