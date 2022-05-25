from sympy import solve, solveset, symbols, pprint, init_printing

init_printing(use_unicode=True)

x = symbols('x')

f1 = x > 10
f2 = x < 20

pprint(f1)
pprint(f2)

print()

solution = solve((f1, f2), x)
pprint(solution)
