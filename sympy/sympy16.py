import sympy as sp

x, y = sp.symbols("x,y")
expression = sp.expand((x - y) * (x + y))
sp.pprint(expression)
