from sympy import solveset, symbols, pprint, init_printing, cos

init_printing(use_unicode=True)

x = symbols("x")

f = cos(x)

pprint(f)

solution = solveset(f, x)
pprint(solution)
