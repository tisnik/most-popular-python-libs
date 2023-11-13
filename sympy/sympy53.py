from sympy import symbols, limit, pprint

x = symbols("x")
f = 1 / x

pprint(limit(f, x, 0, "+"))
