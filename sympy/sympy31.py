from sympy import cos, init_printing, pprint, solve, symbols

init_printing(use_unicode=True)

x = symbols("x")

f = cos(x)

pprint(f)

solution = solve(f, x)
pprint(solution)
