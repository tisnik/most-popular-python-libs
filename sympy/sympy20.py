from sympy import init_printing, pprint, solve, symbols

init_printing(use_unicode=False)

a, b, c, x = symbols("a,b,c,x")

f = a * x ** 2 + b * x + c

pprint(f)

solution = solve(f, x)
pprint(solution)
