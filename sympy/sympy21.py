from sympy import solve, symbols, pprint

a, b, c, d, e, x, y = symbols("a,b,c,d,e,x,y")

f = a * x ** 2 + b * x + c * y ** 2 + d * y + e

pprint(f)

solution = solve(f, x)
pprint(solution)

solution = solve(f, y)
pprint(solution)
