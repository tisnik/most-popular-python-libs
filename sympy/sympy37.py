from sympy import init_printing, pprint, solve, symbols

init_printing(use_unicode=True)

x = symbols("x")

f1 = x ** 2 < 10
f2 = x ** 3 > -10

pprint(f1)
pprint(f2)

print()

solution = solve((f1, f2), x)
pprint(solution)
