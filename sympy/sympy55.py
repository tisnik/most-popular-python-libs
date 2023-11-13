from sympy import symbols, limit, pprint, oo

x = symbols("x")
f = 1 / x

pprint(limit(f, x, oo))
