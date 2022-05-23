import sympy as sp

x,y = sp.symbols('x,y')
expression = sp.factor(x**2 - y ** 2)
sp.pprint(expression)
