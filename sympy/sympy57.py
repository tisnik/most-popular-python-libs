from sympy import symbols, sin, limit, pprint

x = symbols("x")
f = sin(1 / x)

pprint(limit(f, x, 0, "+"))
