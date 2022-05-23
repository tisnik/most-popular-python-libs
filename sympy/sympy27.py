from sympy import solve, symbols, pprint, init_printing

init_printing(use_unicode=True)

x = symbols('x')

f = 5*x**2 + 5*x + 1

pprint(f)

solution = solve(f, x)
pprint(solution)
