#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pandas

s = pandas.Series((1, 2, None, 4, 5, 6), ('a', 'b', 'c', 'd', 'e', 'f'))

print("sum", s.sum(), sep="\t")
print("prod", s.prod(), sep="\t")
print("min", s.min(), sep="\t")
print("max", s.max(), sep="\t")
print("median", s.median(), sep="\t")
print("std", s.std(), sep="\t")
print("var", s.var(), sep="\t")
print("quantile", s.quantile(0.01), sep="\t")
