import sympy as sp

x = sp.symbols("x")
expression = sp.factor(x ** 2 - 2 * x + 1)
sp.pprint(expression)
