#!/usr/bin/python
# vim: set fileencoding=utf-8

from libcst import parse_module
from libcst.tool import dump


expression = "1  + 2"

parsed = parse_module(expression)
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
