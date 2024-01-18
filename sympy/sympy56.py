from sympy import limit, oo, pprint, symbols

x = symbols("x")
f = 1 / x

pprint(limit(f, x, -oo))
