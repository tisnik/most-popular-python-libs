from sympy import init_printing, pprint, solve, symbols

init_printing(use_unicode=True)

x = symbols("x")

f = 5 * x ** 2 + 5 * x + 5

pprint(f)

solution = solve(f, x)
pprint(solution)
