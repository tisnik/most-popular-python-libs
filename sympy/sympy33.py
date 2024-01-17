from sympy import init_printing, pprint, sin, solve, solveset, symbols

init_printing(use_unicode=True)

x = symbols("x")

f = sin(x) / x

pprint(f)

print()

solution = solve(f, x)
pprint(solution)

print()

solution = solveset(f, x)
pprint(solution)
