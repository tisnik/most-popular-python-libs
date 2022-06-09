from sympy import singularities, symbols, pprint, sin

a, b, c, d, e, x = symbols("a,b,c,d,e,x")

f = 1 / (sin(x) - x ** 2)

pprint(f)

print()

s = singularities(f, x)
pprint(s)
