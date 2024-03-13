#!/usr/bin/python
# vim: set fileencoding=utf-8

from libcst import parse_module, CSTTransformer
from libcst import SimpleWhitespace, Name
from difflib import unified_diff


class FunctionRenamer(CSTTransformer):
    def __init__(self, orig_name, new_name):
        self.orig_name = orig_name
        self.new_name = new_name

    def on_visit(self, node):
        return True

    def leave_FunctionDef(self, original_node, updated_node):
        print("Function definition: ", original_node.name.value)
        if original_node.name.value == self.orig_name:
            print(f"Renaming '{self.orig_name}' to '{self.new_name}'")
            return updated_node.with_changes(
                    name=Name(self.new_name))
        return original_node

    def leave_Call(self, original_node, updated_node):
        print("Function call: ", original_node.func.value)
        if original_node.func.value == self.orig_name:
            print(f"Renaming '{self.orig_name}' to '{self.new_name}'")
            return updated_node.with_changes(
                    func=Name(self.new_name))
        return original_node


code = '''
def A(m: int, n: int) -> int:
    """Ackermannova funkce."""
    if m == 0:
        return n + 1
    if n == 0:
        return A(m - 1, 1)
    return A(m - 1, A(m, n - 1))
'''

parsed = parse_module(code)
transformer = FunctionRenamer("A", "ackermann")
transformed = parsed.visit(transformer)

print()
print("-" * 60)
print(parsed.code)
print(transformed.code)

diff = "".join(unified_diff(parsed.code.splitlines(1), transformed.code.splitlines(1)))
print(diff)
