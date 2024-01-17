from sympy import pprint, solve, symbols

a, b, c, x = symbols("a,b,c,x")

f = a * x ** 2 + b * x + c

pprint(f)

solution = solve(f, x)
pprint(solution)
