#!/usr/bin/python
# vim: set fileencoding=utf-8

from libcst import parse_module
from libcst.tool import dump


module = """
def add(x, y):
    return x + y
"""

parsed = parse_module(module)
print("Parsed:")
print(parsed)

print()

dumped = dump(parsed)
print("Dumped:")
print(dumped)

print()

code = parsed.code
print("Code:")
print(code)
