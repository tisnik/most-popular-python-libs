from pint import UnitRegistry
from sympy import pprint, solve, Symbol

ureg = UnitRegistry()

a = Symbol("a") * ureg.meter
b = Symbol("b") * ureg.meter
c = Symbol("c") * ureg.meter

x = Symbol("x")

f = a * x ** 2 + b * x + c

print(f)
print()

solution = solve(f, x)
pprint(solution)
