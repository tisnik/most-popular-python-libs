#!/usr/bin/python
# vim: set fileencoding=utf-8

from libcst import parse_expression
from libcst.tool import dump


expression = "6 * 7"

parsed = parse_expression(expression)
print("Parsed:")
print(parsed)

print()

dumped = dump(parsed)
print("Dumped:")
print(dumped)
