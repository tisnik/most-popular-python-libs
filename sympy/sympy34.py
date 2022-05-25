from sympy import solve, solveset, symbols, pprint, init_printing

init_printing(use_unicode=True)

x = symbols('x')

f = x > 10

pprint(f)

print()

solution = solve(f, x)
pprint(solution)

print()

solution = solveset(f, x)
pprint(solution)
