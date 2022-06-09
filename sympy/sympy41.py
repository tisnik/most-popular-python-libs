from sympy import diff, symbols, pprint

a, b, c, d, e, x, y, z, w = symbols("a, b, c, d, e, x, y, z, w")

f = a * x ** b + c * y ** d + e / z

pprint(f)

print()

diff1 = diff(f, x)
pprint(diff1)

print()

diff2 = diff(f, y)
pprint(diff2)

print()

diff3 = diff(f, z)
pprint(diff3)

print()

diff4 = diff(f, w)
pprint(diff4)
