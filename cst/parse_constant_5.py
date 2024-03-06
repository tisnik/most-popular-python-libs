#!/usr/bin/python
# vim: set fileencoding=utf-8

from libcst import parse_expression
from libcst.tool import dump


constant = "1+2j"

parsed = parse_expression(constant)
print("Parsed:")
print(parsed)

print()

dumped = dump(parsed)
print("Dumped:")
print(dumped)
