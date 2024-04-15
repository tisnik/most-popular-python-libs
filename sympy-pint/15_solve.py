from sympy import init_printing, pprint, solve, symbols
from sympy.physics.units import second

init_printing(use_unicode=True)

t = symbols("t")

f1 = t > 10 * second
f2 = t < 20 * second

pprint(f1)
pprint(f2)

print()

solution = solve((f1, f2), t)
pprint(solution)
