from sympy import *

x = symbols('x')
f = sin(1/x)

pprint(limit(f, x, 0, '+'))

