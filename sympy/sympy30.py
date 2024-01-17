from sympy import init_printing, pprint, solve, symbols

init_printing(use_unicode=True)

x = symbols("x")

f = x ** 10 + 1

pprint(f)

solution = solve(f, x)
pprint(solution)
