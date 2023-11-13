from sympy import symbols, sin, cos, sqrt, diff, pprint

a, b, c, d, e, x, y = symbols("a,b,c,d,e,x,y")

f = a * sin(x ** 2) / b * cos(y ** 2) + c * sqrt(x + y * d) + e

pprint(f)

diff1 = diff(f, x)
pprint(diff1)

diff2 = diff(f, y)
pprint(diff2)
