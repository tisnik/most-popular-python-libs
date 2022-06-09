import sympy as sp

x = sp.symbols("x")
expression = x ** 1 / 1 + x ** 3 / 3 + x ** 5 / 5 + 2 ** (x / 2 + 1)
sp.pprint(expression)
