from sympy import init_printing, pprint, solve, solveset, symbols
from pint import UnitRegistry
from sympy.physics.units import meter

ureg = UnitRegistry()


init_printing(use_unicode=True)

x = symbols("x")

f = x > 10 * meter

pprint(f)

print()

solution = solve(f, x)
pprint(solution)

print()

solution = solveset(f, x)
pprint(solution)
