from sympy import limit, pprint, sin, symbols

x = symbols("x")
f = sin(1 / x)

pprint(limit(f, x, 0, "+"))
