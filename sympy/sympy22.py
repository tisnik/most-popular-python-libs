from sympy import diff, symbols, pprint

a, b, c, d, e, x, y = symbols('a,b,c,d,e,x,y')

f = a*x**2 + b*x + c*y**2 + d*y + e

pprint(f)

diff1 = diff(f, x)
pprint(diff1)

diff2 = diff(f, y)
pprint(diff2)
