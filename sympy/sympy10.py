import sympy as sp

x,y,z = sp.symbols('x,y,z')
expression = 2*x + 3*y + 3*x + y + 1/z + 3/z
sp.pprint(expression)
