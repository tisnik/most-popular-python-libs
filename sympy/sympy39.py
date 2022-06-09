from sympy import diff, symbols, pprint

a, b, c, d, e, x = symbols("a,b,c,d,e,x")

f = a * x ** 3 + b * x ** 2 + c * x + d + e / x

pprint(f)

print()

diff1 = diff(f, x)
pprint(diff1)
