from sympy import *

x = symbols('x')
f = 1/x

pprint(limit(f, x, -oo))

