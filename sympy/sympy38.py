from sympy import diff, pprint, symbols

x = symbols("x")

f = 5 * x ** 3 + 4 * x ** 2 + 3 * x + 4 + 1 / x

pprint(f)

print()

diff1 = diff(f, x)
pprint(diff1)
