from sympy import pprint, singularities, symbols

a, b, c, d, e, x = symbols("a,b,c,d,e,x")

f = 1 / (x ** 2 - 1)

pprint(f)

print()

s = singularities(f, x)
pprint(s)
