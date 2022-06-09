from sympy import solve, symbols, pprint, init_printing, cos

init_printing(use_unicode=True)

x = symbols("x")

f = cos(x)

pprint(f)

solution = solve(f, x)
pprint(solution)
