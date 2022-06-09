from sympy import integrate, symbols, pprint

a, b, c, d, e, x, y = symbols("a,b,c,d,e,x,y")

f = a * x ** 2 + b * x + c * y ** 2 + d * y + e

pprint(f)

solution = integrate(f, x)
pprint(solution)

solution = integrate(f, y)
pprint(solution)
