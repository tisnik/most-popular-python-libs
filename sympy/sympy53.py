from sympy import limit, pprint, symbols

x = symbols("x")
f = 1 / x

pprint(limit(f, x, 0, "+"))
