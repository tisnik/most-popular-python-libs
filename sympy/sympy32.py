from sympy import cos, init_printing, pprint, solveset, symbols

init_printing(use_unicode=True)

x = symbols("x")

f = cos(x)

pprint(f)

solution = solveset(f, x)
pprint(solution)
