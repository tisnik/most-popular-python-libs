import sympy as sp

x,y,z = sp.symbols('x,y,z')
expression = sp.expand((x-y) * (x+y) * (x+z) * (y-z))
sp.pprint(expression)
